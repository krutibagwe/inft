add = \x y -> x+y
sub = \x y -> x-y
mult = \x y -> x*y
div1 = \x y -> x/y
expo = \x y -> x**y
sqrt1 = \x  -> sqrt(x)
addsqrt = \x y -> sqrt(x+y)

main = do
    putStrLn "Enter two numbers (a and b): "
    a<- readLn
    b<- readLn
    print(add a b)
    print(sub a b)
    print(mult a b)
    print(div1 a b)
    print(expo a b)
    print(sqrt1 a)
    print(addsqrt a b)
    
