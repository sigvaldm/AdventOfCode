import Numeric (readHex, showIntAtBase)
import Data.Char (intToDigit, digitToInt)
import Text.ParserCombinators.Parsec

data Packet = Literal { version :: Int , value :: Int }
            | Operator { version :: Int , subpackets :: [Packet] }
              deriving (Show)
    
hexToBin :: String -> String
hexToBin hex = showIntAtBase 2 intToDigit dec ""
    where dec = fst . head . readHex $ hex

binToInt :: String -> Int
binToInt' [] = 0
binToInt' (x : xs) = (digitToInt x) + 2 * binToInt' xs
binToInt = binToInt'.reverse

main = do
    input <- readFile "input"
    let bin = hexToBin input
    let Right ps = parse pPacket "" bin
    print $ versionSum ps

versionSum :: Packet -> Int
versionSum a = case a of
    Literal ver _ -> ver
    Operator ver sub -> ver + sum (map versionSum sub)

pPacket = try pLiteral <|> pOperator

pLiteral = do
    ver <- pVersion
    string "100"
    chunks <- many (char '1' *> count 4 digit)
    last_chunk <- char '0' *> count 4 digit
    let value = binToInt . concat $ (chunks ++ [last_chunk])
    return (Literal ver value)

pOperator = try pOperatorLen <|> pOperatorNum

pOperatorLen = do
    ver <- pVersion
    count 3 digit
    char '0'
    len <- binToInt <$> count 15 digit
    str <- count len digit
    let Right packets = parse (many pPacket) "" str
    return (Operator ver packets)

pOperatorNum = do
    ver <- pVersion
    count 3 digit
    char '1'
    num <- binToInt <$> count 11 digit
    packets <- count num pPacket
    return (Operator ver packets)

pVersion = binToInt <$> count 3 digit
