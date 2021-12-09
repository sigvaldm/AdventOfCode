main = do

    -- Read list of numbers from file
    input <- readFile "input.txt"
    let l = map read (words input) :: [Int]

    -- Compute and print result
    let (a,b) = head [(x,y) | x<-l, y<-l, x+y==2020]
    print (a*b)

    -- Compute and print result
    let (a,b,c) = head [(x,y,z) | x<-l, y<-l, z<-l, x+y+z==2020]
    print (a*b*c)
