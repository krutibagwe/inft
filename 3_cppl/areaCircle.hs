areaCircle::Float-> Float
areaCircle x = pi*x*x

main = do
    putStrLn "Enter radius: "
    a<- readLn
    putStrLn "Area of circle: "
    print(areaCircle a)
