import Data.List (transpose)
import Data.Char (digitToInt)

-- List of binary integers to integer
binToInt' [] = 0
binToInt' (x : xs) = (digitToInt x) + 2 * binToInt' xs
binToInt = binToInt'.reverse

findRate [x] result op = result++x
findRate xs result op = do
    let numOnes = length $ filter ((=='1') . head) xs
    let chosen = if (2*numOnes) `op` (length xs) then '1' else '0'
    let ys = filter h xs where h x = head x == chosen
    let zs = map (drop 1) ys
    let new_result = result ++ [chosen]
    findRate zs new_result op

main = do
    input <- readFile "input"
    let lines = words input
    let oxygenRate = binToInt $ findRate lines "" (>=)
    let carbRate = binToInt $ findRate lines "" (<)
    print (oxygenRate*carbRate)
