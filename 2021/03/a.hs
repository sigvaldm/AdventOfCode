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

main = do
    input <- readFile "input"
    let columns = transpose (words input)
    let gamma = map convertStr columns
    let epsilon = map complement gamma where complement 0 = 1
                                             complement 1 = 0

    print $ (binToInt gamma) * (binToInt epsilon)
