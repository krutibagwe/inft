doublePost::[Int]->[Int]
doublePost xs = [x*2|x<-xs,x>0]

main=do
    putStrLn ("Original List: ")
    print([-1,2,6,-99,7])
    putStrLn ("Doubled positive numbers are: ")
    print(doublePost[-1,2,6,-99,7])
