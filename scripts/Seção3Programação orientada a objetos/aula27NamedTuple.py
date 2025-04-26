# são quase iguais as classes, serão utilizadas quando você for fazer uma classe que n tenha metodos nem nada
from collections import namedtuple

cartas_ = namedtuple("carta", ["valor", "naipe"]) # quero uma carta, q nessa carta tem valor e naipe
carta1 = cartas_("A", "Espadas")

print(carta1)