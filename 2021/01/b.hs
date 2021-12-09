main = do

    -- Read list of numbers from file
    input <- readFile "input.txt"
    let l = map read (words input) :: [Int]

    let averages = map (\(a,b,c)->a+b+c) $ zip3 (init l) (init (tail l)) (tail (tail l))

    let increases = zipWith (>) (tail averages) (init averages)
    let countTrue = length . filter (==True)
    print $ countTrue increases
