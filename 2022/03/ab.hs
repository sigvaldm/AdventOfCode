-- Compile with Glasgow Haskell Compiler and execute:
--      $ ghc ab.hs; ./ab

import Data.List -- nub
import Data.Char -- ord, isLower

main = do
    rucksacks <- fmap lines $ readFile "input.txt"
    let sharedItems = map (intersection.splitAtHalf) rucksacks
    print $ sum $ map toPriority sharedItems
    print $ sum $ map toPriority (intersectionBy3 rucksacks)

intersection (xs,ys) = nub $ filter (\x -> x `elem` xs) ys

intersectionBy3 [] = []
intersectionBy3 (x:y:z:rest) = inter3 (x,y,z) : intersectionBy3 rest
    where inter3 (x,y,z) = intersection (x,intersection (y,z))

splitAtHalf xs = splitAt ((length xs) `div` 2) xs
toPriority (c:_)
    | isLower(c) = (ord c) - (ord 'a') + 1
    | otherwise = (ord c) - (ord 'A') + 27
