areaTriangle::Float-> Float-> Float
areaTriangle x y = 0.5*x*y 

main = do
    putStrLn "Enter base and height: "
    a<- readLn
    b<- readLn
    putStrLn "Area of triangle: "
    print(areaTriangle a b)
