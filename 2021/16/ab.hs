import Numeric (readHex, showIntAtBase)
import Data.Char (intToDigit, digitToInt)
import Text.ParserCombinators.Parsec

data Packet = Literal { version :: Int , value :: Int }
            | Operator { version :: Int , op :: Op, subpackets :: [Packet] }
              deriving (Show)

data Op = Sum | Product | Min | Max | CGT | CLT | CEQ deriving (Show)
    
hexToBin :: String -> String
hexToBin [] = ""
hexToBin (x:xs) = m ++ hexToBin xs
    where m = case x of
            '0' -> "0000"
            '1' -> "0001"
            '2' -> "0010"
            '3' -> "0011"
            '4' -> "0100"
            '5' -> "0101"
            '6' -> "0110"
            '7' -> "0111"
            '8' -> "1000"
            '9' -> "1001"
            'A' -> "1010"
            'B' -> "1011"
            'C' -> "1100"
            'D' -> "1101"
            'E' -> "1110"
            'F' -> "1111"


binToInt :: String -> Int
binToInt' [] = 0
binToInt' (x : xs) = (digitToInt x) + 2 * binToInt' xs
binToInt = binToInt'.reverse

main = do
    input <- readFile "input"
    let bin = hexToBin input
    let Right ps = parse pPacket "" bin
    print $ versionSum ps
    print $ execute ps

versionSum :: Packet -> Int
versionSum a = case a of
    Literal ver _ -> ver
    Operator ver _ sub -> ver + sum (map versionSum sub)

execute :: Packet -> Int
execute (Literal _ v) = v
execute (Operator _ Sum ps) = sum (map execute ps)
execute (Operator _ Product ps) = product (map execute ps)
execute (Operator _ Min ps) = minimum (map execute ps)
execute (Operator _ Max ps) = maximum (map execute ps)
execute (Operator _ CGT (a:b:[])) = if (execute a) > (execute b) then 1 else 0
execute (Operator _ CLT (a:b:[])) = if (execute a) < (execute b) then 1 else 0
execute (Operator _ CEQ (a:b:[])) = if (execute a) == (execute b) then 1 else 0

pPacket = try pLiteral <|> pOperator

pLiteral = do
    ver <- pVersion
    string "100"
    chunks <- many (char '1' *> count 4 digit)
    last_chunk <- char '0' *> count 4 digit
    let value = binToInt . concat $ (chunks ++ [last_chunk])
    return (Literal ver value)

pOperator = try pOperatorLen <|> pOperatorNum
-- pOperator = pOperatorLen

pOperatorLen = do
    ver <- pVersion
    op <- pOp
    char '0'
    len <- binToInt <$> count 15 digit
    str <- count len digit
    let Right packets = parse (many pPacket) "" str
    return (Operator ver op packets)

pOperatorNum = do
    ver <- pVersion
    op <- pOp
    char '1'
    num <- binToInt <$> count 11 digit
    packets <- count num pPacket
    return (Operator ver op packets)

pVersion = binToInt <$> count 3 digit
pOp = do
    a <- binToInt <$> count 3 digit
    case a of
        0 -> return Sum
        1 -> return Product
        2 -> return Min
        3 -> return Max
        5 -> return CGT
        6 -> return CLT
        7 -> return CEQ
