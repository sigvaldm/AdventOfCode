import Data.List (transpose)

-- List of binary integers to integer
binToInt' [] = 0
binToInt' (x : xs) = x + 2 * binToInt' xs
binToInt = binToInt'.reverse

-- Convert strings "001011" to 0 or 1 depending on majority count
convertStr s
    | 2*(countOnes s) < (length s) = 0
    | otherwise                    = 1
    where countOnes = length . filter (== '1')

countOnes = length . filter (== '1') . head
chooseMajority xs = if 2*(countOnes xs) >= length xs then '1' else '0'
chooseMinority xs = if 2*(countOnes xs) < length xs  then '0' else '1'

findRate :: [String] -> String -> ([String]->Char) -> String
findRate [x] result predicate = result++x
findRate xs result predicate = do
    -- let numOnes = length $ filter ((=='1').head) xs
    -- let majority = if 2*numOnes >= length xs
    --                then '1'
    --                else '0'
    let majority = predicate xs
    let ys = filter h xs where h x = head x == majority
    let zs = map (drop 1) ys
    let new_result = result ++ [majority]
    findRate zs new_result predicate

main = do
    input <- readFile "dummy"
    let lines = words input
    -- let x = filter h lines where h x = head x == '0'
    print $ findRate lines "" chooseMajority
    -- print $ chooseMajority ["0101", "0000", "1001", "1111"]
    -- print lines
    -- print x
    -- print $ findRate $ findRate lines
