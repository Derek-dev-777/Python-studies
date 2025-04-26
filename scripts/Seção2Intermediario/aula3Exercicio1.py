
def multiplicação(*args):
    total = 1
    for numeros in args:
        
        total = total * numeros
    return total

def par_ou_impar(number):
    
    avaliação = number % 2
    if avaliação == 0:
        print("O numero é par")
    else:
        print("O numero é impar")



multiplicação1 = multiplicação(5,10,25,10)
print(multiplicação1)

par = par_ou_impar(2)
print(par_ou_impar)