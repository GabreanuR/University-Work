element_of(X,[X|_]).
element_of(X,[_|Tail]) :- element_of(X,Tail).

concat_lists([], List, List).
concat_lists([Elem | List1], List2, [Elem | List3]) :- concat_lists(List1, List2, List3).

all_a([a]).
all_a([a|Tail]) :- all_a(Tail).

trans_a_b([],[]).
trans_a_b([a|T1],[b|T2]) :- trans_a_b(T1,T2). 

sc(_,[],[]).
% sc(X,[H|T],Rez) :- V is X*H, sc(X,T,Rezp), Rez = [V|Rezp].
sc(X,[H|T],[V|Rez]) :- V is X*H, sc(X,T,Rez).

% nusc(_,[],[]).
% nusc(X,[H|T],[X*H|Rez]) :- nusc(X,T,Rez).

dot([],[],0).
dot([X|Y],[A|B],Rez) :- dot(Y,B,Rezp), Rez is X*A+Rezp.

max([],0).
max([H|T],Y) :- max(T,Y), Y>=H.
max([H|T],H) :- max(T,Y), Y<H.