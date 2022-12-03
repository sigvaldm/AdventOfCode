import Data.List -- nub
import Data.Char -- ord, isLower

main = do
    input <- readFile "input.txt"
    let sharedItems = map (intersection.splitAtHalf) (lines input)
    print $ sum $ map toPriority sharedItems

intersection (xs,ys) = nub $ filter (\x -> x `elem` xs) ys
splitAtHalf xs = splitAt ((length xs) `div` 2) xs
toPriority (c:_)
    | isLower(c) = (ord c) - (ord 'a') + 1
    | otherwise = (ord c) - (ord 'A') + 27
