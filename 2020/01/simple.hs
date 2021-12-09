ls = [1721, 979, 366, 299, 675, 1456]
-- (a,b) = head [(x,y) | x <- ls, y <- ls, x+y==2020]

main = print (a*b) where (a,b) = head [(x,y) | x <- ls, y <- ls, x+y==2020]
