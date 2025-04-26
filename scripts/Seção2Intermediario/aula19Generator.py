import sys

# Generation

generator = [n for n in range(100)] # a lista esta inteira na memoria
generator_leve = ( n for n in range(100)) # o generator não esta, ele tem q ser apresentado 1 por um

print(sys.getsizeof(generator_leve)) # mostra o tanto de memorioa q as variaveis estão ocupando
print(sys.getsizeof(generator))

for n in generator_leve: # usando o generator, você ocupa bem menos memoria e aplica em certos casos a mesma coisa
    print(n)

# Exemplo de generator:

def generator(n=0, maximum=10):
    yield n
    n += 1

    if n >= maximum:
        return
    
gen = generator(maximum= 100)

for i in gen:
    print(i)    