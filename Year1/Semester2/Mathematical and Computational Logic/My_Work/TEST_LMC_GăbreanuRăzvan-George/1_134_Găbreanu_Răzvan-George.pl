%Varianta 1
%Grupa 134
%Găbreanu Răzvan-George

%EX1
%Parcurgem recursiv lista, actualizand HR in functie relatia dintre X si Y.
%Daca X<Y, trebuie sa adaugam intervalul (X,Y).
%daca X>Y, trebuie sa aduagam lista vida.
%Daca X=Y, trebuie sa adaugam doar X.
expand_intervals([],[]).
expand_intervals([(X,Y)|T],[HR|TR]) :- X < Y, HR = [X], M is X+1, 
    expand_intervals([(M,Y)|T],TR).
expand_intervals([(X,Y)|T],[HR|TR]) :- X > Y, HR = [], expand_intervals(T,TR).
expand_intervals([(X,Y)|T],[HR|TR]) :- X = Y, HR = [X], expand_intervals(T,TR).
/*
Pentru: expand_intervals([(1, 3), (5, 5), (5, 3), (2, 6)], R).

Rezultatul:
R = [[1], [2], [3], [5], [], [2], [3], [4], [5], [6]]
false
*/

%EX2
%Verificam daca cele doua siruri sunt egale (atunci cand ajungem div_concat([],[]).), 
%folosind functia auxiliara iden(X,Y). Concatenam cele 2 siruri.
div_concat([],[]).
div_concat([HL|TL],[HR|TR]) :- iden(HL,HR), div_concat(TL,TR).
div_concat([HL|TL],[HR|TR]) :- not(iden(HL,HR)), M = [HR|TR], append(TL, HL, M).

%Testam egalitatea, nu unificam termenii
iden(X,Y) :- X == Y.
/*
Pentru: div_concat(R, [1, 2, 3, 4, 5, 6, 7, 8, 9]).

Rezultatul:
R = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
R = [[2, 3, 4, 5, 6, 7, 8, 9], 1]
R = [[3, 4, 5, 6, 7, 8, 9], 1, 2]
R = [[4, 5, 6, 7, 8, 9], 1, 2, 3]
R = [[5, 6, 7, 8, 9], 1, 2, 3, 4]
R = [[6, 7, 8, 9], 1, 2, 3, 4, 5]
R = [[7, 8, 9], 1, 2, 3, 4, 5, 6]
R = [[8, 9], 1, 2, 3, 4, 5, 6, 7]
R = [[9], 1, 2, 3, 4, 5, 6, 7, 8]
R = [[], 1, 2, 3, 4, 5, 6, 7, 8, 9]
false

Pentru div_concat([1, 2, 3], [2, 1, 3]).

Rezultatul:
false
*/