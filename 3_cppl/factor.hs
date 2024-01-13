factor::Int->[Int]
factor n =[x|x<-[1..n], (n `mod` x ==0) && (x/=1) && (x/=n)]

main = do
    putStrLn "Enter the number n: "
    n<-readLn
    print(factor n)
