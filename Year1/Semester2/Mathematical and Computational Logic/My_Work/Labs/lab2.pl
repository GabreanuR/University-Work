distance((Xa,Ya),(Xb,Yb),D):- D is sqrt((Xa-Xb)**2+(Ya-Yb)**2).
fib(0,1).
fib(1,1).
fib(N,X) :- N > 1, M is N-1, fib(M,Y), P is N-2, fib(P,Z), X is Y+Z.

fibo(0,0,1).
fibo(1,1,1).
fibo(N,Z,X) :- N > 1, M is N-1, fibo(M,Y,Z), X is Y+Z.

fibg(N,X):-fibo(N,_,X).

line(0,_).
line(X,C):-X>0,Y is X-1, write(C), line(Y,C).

rectangle(0,_,_):-nl.
rectangle(X,Z,C):-X>0,line(Z,C),nl,Y is X-1, rectangle(Y,Z,C).

square(X,C):-rectangle(X,X,C).
square2(X,C):-Y is X+4, rectangle(X,Y,C).