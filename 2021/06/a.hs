import Data.List (break)

-- split comma-separated string to list
split str = case break (`elem` [',','\n']) str of
    (a,',':b) -> a : split b
    (a,'\n':_) -> [a]


next :: [Int] -> [Int]
next state = updated ++ appendage
    where
      f x = if x==0 then 7 else x
      updated' = map f state
      updated = map (\a -> a-1) updated'
      numZeroes = length $ filter (==0) state
      appendage = take numZeroes $ repeat 8

main = do
    input <- readFile "input"
    let state = map read (split input) :: [Int]
    let all_states = iterate next state -- The state for all future times
    print $ length (all_states!!80)
