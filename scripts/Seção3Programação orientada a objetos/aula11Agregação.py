

class Carrinho:
    
    def __init__(self):
        self._produtos = []

    # função de somar o preço do produto de cada produto dentro da lista "self.produtos"
    def total(self):
        return sum([p.preco for p in self._produtos])# produto preço, para produtos in self.produtos
    
    #função para inserir produtos, observe o "*produtos", é utilizado pois os produtos tem nome e preço, e queremos
    # ambos
    def inserirProduto(self, *produtos):
        for produto in produtos: 
            self._produtos.append(produto) # append funciona nas listas criadas dentro das classes

    # função para listar os produtos dentro de self.produtos
    def listarProdutos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco) # desempacotamento

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1 = Produto("Caneta", 1.20)
p2 = Produto('Doritos', 15)

carrinho.inserirProduto(p1, p2)
carrinho.listarProdutos()
print(carrinho.total())
        