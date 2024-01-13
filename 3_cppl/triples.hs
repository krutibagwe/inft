triples::Int->[(Int,Int,Int)]
triples n=[(x,y,z)|x<-[1..n], y<-[1..n], z<-[1..n], x^2+y^2==z^2]

main = do
    putStrLn "Enter the number n:"
    n<- readLn
    print(triples n)
