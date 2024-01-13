divByTen ::(Fractional a)=> a-> a
divByTen x = x/10

main::IO()
main = do
    putStrLn "Enter a number: "
    x<- readLn
    print(divByTen x)
