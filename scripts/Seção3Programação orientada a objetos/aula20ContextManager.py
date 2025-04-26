

class Myopen: # função para inicializar arquivos e fecha-los corretamente

    def __init__(self, caminho_arquivo, modo): # passa o caminho do arquivo e modo que deve ser lido ou escrito
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None # variavel para atribuir o arquivo 

    def __enter__(self):
        print("enter")
        self._arquivo = open(self.caminho_arquivo, self.modo) # como se fosse um with open
        return self._arquivo # retorna arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print("Exit")
        self._arquivo.close() # e aqui ele se certifica de fechar meu arquivo



with Myopen("aula20ContextManager.txt", "w") as sei_la: # o retorno do "__enter__" vai para dentro da variavel "sei_la"
    sei_la.write("Linha 1")
    sei_la.write("Linha 4")
    sei_la.write("Linha 3")
    sei_la.write("Linha 2")
    print("With", sei_la)
