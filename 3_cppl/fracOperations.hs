import Data.Ratio

main::IO()
main=do

    putStrLn"Enter the numerator of 1st number: "
    numerator1 <- readLn
    putStrLn"Enter the denominator of 1st number: "
    denominator1 <- readLn
    putStrLn"Enter the numerator of 2nd number: "
    numerator2 <- readLn
    putStrLn"Enter the denominator of 2nd number: "
    denominator2 <- readLn

    let fraction1 = numerator1 % denominator1
        fraction2 = numerator2 % denominator2
        
    putStrLn"Addition of fractions: "
    print (fraction1 + fraction2)
    
    putStrLn"Subtraction of two fractions: "
    print(fraction1 - fraction2)
    
    putStrLn"Multiplication of fractions: "
    print (fraction1 * fraction2)
    
