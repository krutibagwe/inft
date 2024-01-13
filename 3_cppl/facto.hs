facto::Int->Int
facto 0=1
facto n= n*facto(n-1)

main = do
    putStrLn "Enter the value of n: "
    a<-readLn
    putStrLn "Factorial: "
    print(facto a)
