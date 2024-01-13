facto(0,1).
facto(N,Result):-
    N>0,
    N1 is N-1,
    facto(N1,Result1),
    Result is Result1*N. 
        
