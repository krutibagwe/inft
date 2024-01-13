sum1(0,0).
sum1(N,Result):- 
    N>0;
    N1 is N-1,
    sum1(N1,Result),
    Result is Result1+N.
