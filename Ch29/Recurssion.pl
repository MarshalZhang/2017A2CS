factorial(1,1).
factorial(N,F):-
  M is N-1,
  factorial(M,X),
  F is N*X.


bunnyEars(1,2).
bunnyEars(N,F):-
  bunnyEars(N-1, X),
  F is 2+X.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(N,F):-
   fibonacci(N-1, X),
   fibonacci(N-2, Z).
   F is X+Z

bunnyEars(0,0).
bunnyEars(1,2).
bunnyEars(N,F):-
   