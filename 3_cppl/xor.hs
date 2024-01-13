xor :: Bool -> Bool -> Bool
xor a b = (a || b) && not (a && b)

main :: IO ()
main = do
    putStrLn "Enter True or False: "
    a<- readLn
    putStrLn "Enter True or False: "
    b<- readLn
    print(xor a b)
    
     
