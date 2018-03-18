cat(jack).
cat(black).
dog(Billy).
dog(Rex).

animal(X): -dog(X).
animal(X): -cat(X).
enimies(X,Y): -(cat(X), dog(Y)).
enimies(X,Y): -(cat(Y), dog(X)).

male(john).
male(jack).
male(bill).
male(jimmy).
female(mary).
female(elisabth).
female(kids).

parent(bill,mary).
parent(kirs,bill).
parent(jimmy, bill).
parent(elisabeth,mary).