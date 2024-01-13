revString::String->String
revString [x]=[x]
revString (x:xs)= revString xs ++ [x]

main = do
    print(revString"hello")
