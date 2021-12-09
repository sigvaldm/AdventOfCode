main = do

    -- Read list of numbers from file
    input <- readFile "input.txt"
    let l = map read (words input) :: [Int]

    let increases = zipWith (>) (tail l) (init l)
    let countTrue = length . filter (==True)
    print $ countTrue increases
