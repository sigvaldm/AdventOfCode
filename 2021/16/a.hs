import Numeric (readHex, showIntAtBase)
import Data.Char (intToDigit, digitToInt)

data Packet = Literal { version :: Int , value :: Int }
            | Operator { version :: Int , subpackets :: [Packet] }
              deriving (Show)
    
main = do
    -- input <- readFile "input"
    -- let input = "D2FE28"
    -- let bin = hexToBin input
    let bin = "110100101111111000101000"
    print $ parsePacket bin

hexToBin :: String -> String
hexToBin hex = showIntAtBase 2 intToDigit dec ""
    where dec = fst . head . readHex $ hex

-- For some reason I don't have readBin
-- binToInt :: String -> Int
-- binToInt = fst . head . readBin

binToInt :: String -> Int
binToInt' [] = 0
binToInt' (x : xs) = (digitToInt x) + 2 * binToInt' xs
binToInt = binToInt'.reverse

parsePacket :: String -> Packet
parsePacket bin = do
    let (version', a) = splitAt 3 bin
    let (typ', b) = splitAt 3 a
    let version = binToInt version'
    let typ = binToInt typ'
    case typ of
        4 -> Literal version (parseChunks b)
        otherwise -> Operator version (parseSubpackets b)

parseChunks :: String -> Int
parseChunks = binToInt . parseChunks'
parseChunks' bin = do
    let ((flag:chunk), remainder) = splitAt 5 bin
    case flag of
        '0' -> chunk
        '1' -> chunk ++ (parseChunks' remainder)

parseSubpackets :: String -> [Packet]
parseSubpackets bin = do
    let (flag:a) = bin
    case flag of
        '0' ->
            let (len, b) = splitAt 15 a
             
