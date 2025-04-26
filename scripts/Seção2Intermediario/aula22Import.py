"""
você pode importar modulos para adicionar funcionalidades para o seu codigo
import nome do modulo (ok)
from nome do modulo import nome da função que você quiser
import (nome) from (nome função) as (costumiza nome)
"""

#exemplo
import importlib
import math # importa inteiro
from math import ceil # importa uma função dentro de math
from math import ceil as arredondar # importa uma função dentro de math e renomeia ela como arredondar

import Exericicioporfora # aqui você pode importar outros modulos, apenas seguido a ordem de uma piramide
# queme stá no topo pode importar todos de baixo, e os de baixo não conseguem alcançar os de cima
importlib.reload(Exericicioporfora) # essa função carrega tudo que esta dentro do codigo quando é chamada
#podendo repeti-la varias vezes