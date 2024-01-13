applyTwice::(a->a)->(a->a)->a->a
applyTwice f1 f2 x= f1(f2 x)

main=do
    putStrLn "Hello World!"
    putStrLn "Enter three numbers: "
    a<- readLn
    b<- readLn
    c<- readLn
    putStrLn "Result: "
    print(applyTwice(*a)(+b)c)
