palindrom1(L):- reverse(L,L).

rev([],[]).
rev([H|T],Rez):- rev(T,R1),append(R1,[H],Rez).

remove_duplicates([],[]).
remove_duplicates([H|T],[H|Rez]):- remove_duplicates(T,Rez),not(member(H,Rez)).
remove_duplicates([H|T],Rez):- remove_duplicates(T,Rez),member(H,Rez).

atimes(_,[],0).
atimes(E,[E|T],Rez) :- atimes(E,T,R1), Rez is R1+1.
atimes(E,[H|T],Rez) :- atimes(E,T,Rez), E\=H.

insert(X,[],[X]).
insert(X,[H|T],[X|[H|T]]) :- X<H.
insert(X,[H|T],[H|Rez]):- X>=H, insert(X,T,Rez).

insertsort([],[]).
insertsort([H|T],L) :- insertsort(T,L1), insert(H,L1,L).

quicksort([],[]).
quicksort([H|T],L) :- split(H,T,A,B), quicksort(A,M), quicksort(B,N), append(M,[H|N],L).
