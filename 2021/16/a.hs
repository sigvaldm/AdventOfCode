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

parsePacket :: String -> (Packet, String)
parsePacket bin = do
    let (version', a) = splitAt 3 bin
    let (typ', b) = splitAt 3 a
    let version = binToInt version'
    let typ = binToInt typ'
    case typ of
        4 -> (Literal version value, remainder)
            where (value, remainder) = parseChunks b
        otherwise ->
            (Literal 999 999, "")
            -- Operator version (parseSubpackets b)

parseChunks :: String -> (Int, String)
parseChunks bin = (binToInt a, b)
    where
        (a, b) = parseChunks' bin
        parseChunks' bin = do
            let ((flag:chunk), remainder) = splitAt 5 bin
            case flag of
                '0' -> (chunk, remainder)
                '1' -> (chunk ++ a, b)
                    where (a, b) = parseChunks' remainder

parseOperator :: String -> ([Packet], String)
parseOperator bin = do
    let (flag:a) = bin
    case flag of
        '0' -> parseSubpacketsLen len b
            where (len, b) = splitAt 15 a
        -- '1' -> parseSubpacketsNum num b
        --     where (num, b) = splitAt 11 a

parseSubpacketsLen :: Int -> String -> ([Packet], String)
parseSubpacketsLen len s = do
    let (p, r) = parsePacket s
    let remLen = (length s) - (length r)
    case remLen of
        0 -> ([p], r)
        otherwise -> (p:ps, rr)
            where (ps, rr) = parseSubpacketsLen remLen r
