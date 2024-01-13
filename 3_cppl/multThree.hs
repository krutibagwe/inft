multThree::(Num a)=>a->a->a->a
multThree x y z= x*y*z

main = do
    putStrLn"Hello World!"
    putStrLn "Enter three numbers: "
    a<- readLn
    b<- readLn
    c<- readLn
    putStrLn "Multiplication: "
    print(multThree a b c)
