import Data.List (transpose)
import Data.Char (digitToInt)

-- List of binary integers to integer
binToInt' [] = 0
binToInt' (x : xs) = (digitToInt x) + 2 * binToInt' xs
binToInt = binToInt'.reverse

countOnes = length . filter ((== '1') . head)
chooseMajority xs = if 2*(countOnes xs) >= length xs then '1' else '0'
chooseMinority xs = if 2*(countOnes xs) >= length xs then '0' else '1'

findRate :: [String] -> String -> ([String]->Char) -> String
findRate [x] result predicate = result++x
findRate xs result predicate = do
    let chosen = predicate xs
    let ys = filter h xs where h x = head x == chosen
    let zs = map (drop 1) ys
    let new_result = result ++ [chosen]
    findRate zs new_result predicate

main = do
    input <- readFile "dummy"
    let lines = words input
    let oxygenRate = binToInt $ findRate lines "" chooseMajority
    let carbRate = binToInt $ findRate lines "" chooseMinority
    print (oxygenRate*carbRate)
