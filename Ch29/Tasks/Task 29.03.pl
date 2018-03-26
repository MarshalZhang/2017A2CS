parent(fred, jack).
parent (fred, alia).
parent(fred, paul).
parent(marshal, rex).
parent(rex, fred).
parent(dave, fred).
grandparent(G, S) :- 
parent(G, P), 
parent(P, S).
sibling(A, B) :- 
parent(P , A), 
parent(P , B).
sibling(A, B) :- 
parent(P, A), 
parent(P , B),
not(A=B).

male(fred).
female(alia).

father(F, C) :- 
male(F), 
parent(F, C).
ancestor(fred,jack).
ancestor(A,jack):-
 ancestor(B, jack),
 parent(A,B).
