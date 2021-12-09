import Text.ParserCombinators.Parsec

data Command = Forward Int
             | Up Int
             | Down Int
               deriving (Show)

main = do
    input <- readFile "input"
    let Right steps = parse inputFile "" input
    let (x,y,a) = foldl inc (0,0,0) steps
    print (x*y)

inc (pos, depth, aim) cmd = case cmd of
    Forward a -> (pos+a, depth+aim*a, aim)
    Up a      -> (pos  , depth      , aim-a)
    Down a    -> (pos  , depth      , aim+a)

inputFile = endBy line (char '\n')
line = forward <|> up <|> down
forward = string "forward " *> (Forward . read <$> many digit)
up      = string "up "      *> (Up      . read <$> many digit)
down    = string "down "    *> (Down    . read <$> many digit)
