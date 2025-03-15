female(mary).
female(sandra).
female(juliet).
female(lisa).
male(peter).
male(paul).
male(dony).
male(bob).
male(harry).
parent(bob, lisa).
parent(bob, paul).
parent(bob, mary).
parent(juliet, lisa).
parent(juliet, paul).
parent(juliet, mary).
parent(peter, harry).
parent(lisa, harry).
parent(mary, dony).
parent(mary, sandra).

father_of(F,C):-parent(F,C),male(F).
mother_of(M,C):-parent(M,C),female(M).
grandfather_of(GF,C):-father_of(GF,P),parent(P,C).
grandmother_of(GM,C):-mother_of(GM,P),parent(P,C).
sister_of(SIS,SIB):-parent(X,SIS),parent(X,SIB),female(SIS),SIS\=SIB.
brother_of(BRO,SIB):-parent(X,SIS),parent(X,SIB),male(BRO),BRO\=SIB.
aunt_of(A,C):-sister_of(A,P),parent(P,C).
uncle_of(U,C):-brother_of(U,P),parent(P,C).

%not_parent(X,Y):-not(parent(X,Y)).

not_parent(X,Y):- (male(X);female(X)),(male(Y);female(Y)),X\=Y,not(parent(X,Y)).