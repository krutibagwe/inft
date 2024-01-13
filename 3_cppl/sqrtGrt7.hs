isSquareRootGreaterThanSeven :: Double -> Bool
isSquareRootGreaterThanSeven x = sqrt x > 7.0

filterSqRoot :: [Double] -> [Double]
filterSqRoot numbers = [x | x <- numbers, isSquareRootGreaterThanSeven x]

main :: IO ()
main = do
    let numbers = [14.0, 169.0, 25.1]
    putStrLn ("Original numbers: " ++ show numbers)
    
    let filtered = filterSqRoot numbers
    putStrLn ("Filtered numbers where square root is greater than seven: " ++ show filtered)
