spaces::Int->String
spaces n = [' '|x<-[1..n]]

main = do
    putStrLn "Enter the number of spaces: "
    a<- readLn
    print(spaces a)
