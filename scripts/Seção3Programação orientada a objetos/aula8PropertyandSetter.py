# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas

#O @property permite que um método seja acessado como se fosse um atributo.
# Isso é útil quando você quer controlar como um valor é calculado ou protegido.

#O @setter permite que você modifique um atributo protegido ( um @property) (self._atributo) com regras personalizadas.

# então primeiro criamos o property como um intermediador entre o objetivo e o setter ( criador de regras)

# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    
    @property       # eu entendi como um meio de atribuir atributos a sua classe
    def cor(self):  # podendo então mudar o nome do atributo deixando mais facil ou colocando oq esta acostumuado
        return self.cor_tinta
    
    # assim podemos montar um "Setter", que serve para alterar / salvar dados na minha property

    @cor.setter
    def cor(self, valor):
        self.cor_tinta = valor
    
caneta = Caneta("Azul")

print(caneta.cor)

caneta.cor = "rosa"