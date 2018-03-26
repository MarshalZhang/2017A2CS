#Task 29.05
#Marshal Zhang from S3C3 option1

factorial(O, 1). 
factorial (N, R):-
M is N - 1,
factorial (M, P),
R is P * N.