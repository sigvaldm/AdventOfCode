-- Compile and run with:
--      $ ghc ab.hs; ./ab

import Data.List

main = do
    input <- readFile "input.txt"
    print $ findMarker input 4 0
    print $ findMarker input 14 0

findMarker (x:xs) size consumed
    | repeated (take size (x:xs)) = findMarker xs size (consumed+1)
    | otherwise = consumed + size
    where repeated xs = xs /= nub xs
