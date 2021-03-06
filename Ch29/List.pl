#Marshal from S3C3 Option1

len([],0).
len([_|T],L):-
         len(T,X),
         L is X +1.

mymember(I,[I|_]).
mymember(I,[_|T]):-
        mymember(I, T).

myappend([a,b],[c,d], [a,b,c,d]).
myappend([],X, X).
myappend([H|T],  L,[H|R]):-
       myappend(T,L,R).	

mylast([b],b).
mylast([_|T],L):-
      mylast(T,L).


add1([],[]).
add1([A|B],[C|D]):-
        add1(B,D),
        C is A+1.

lastbutone([A,_],A).
lastbutone([_|B],R):-
       lastbutone(B,R).

elementat(A,[A|_],1).
elementat(A,[A],1).
elementat(A,[_|T],K):-
       R is K-1,
       elementat(A,T,R).


reverse([A],[A]).
reverse([A|B],L):-
	append(R,[A],L),
	reverse(B,R).
       

palindrome(A):-
    reverse(A,B),
    A==B.

   
     

 


