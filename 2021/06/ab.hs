import Data.List (break)

-- split comma-separated string to list
split str = case break (`elem` [',','\n']) str of
    (a,',':b) -> a : split b
    (a,'\n':_) -> [a]

-- Advance the state vector.
-- The state vector counts how many fish there are with each timer value
next [a,b,c,d,e,f,g,h,i] = [b,c,d,e,f,g,h+a,i,a]
        
main = do
    input <- readFile "input"
    let fish = map read (split input) :: [Int]
    let f x = length (filter (==x) fish)
    let state = [f 0, f 1, f 2, f 3, f 4, f 5, f 6, 0, 0]
    let all_states = iterate next state -- The state for all future times
    print $ sum (all_states!!80)
    print $ sum (all_states!!256)
