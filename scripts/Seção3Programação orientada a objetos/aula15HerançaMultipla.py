
# é a mesma coisa da simples mas...

class A:

    ... 
class B(A):
    ...
class C(B):
    ...

class D(B, C): # aqui ele herda tanto de B e C, tomar cuidado pois isso fica muito complexo no codigo

    ...