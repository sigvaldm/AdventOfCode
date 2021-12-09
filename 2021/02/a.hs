import Text.ParserCombinators.Parsec

main = do
    input <- readFile "input"
    let Right steps = parse inputFile "" input
    let (x,y) = foldl inc (0,0) steps where inc (a,b) (xa,xb) = (xa+a,xb+b)
    print (x*y)

inputFile = endBy line (char '\n')
line = forward <|> up <|> down
forward = string "forward " *> (f <$> many digit) where f x = (read x,0)
up      = string "up "      *> (f <$> many digit) where f x = (0,-read x)
down    = string "down "    *> (f <$> many digit) where f x = (0, read x)
