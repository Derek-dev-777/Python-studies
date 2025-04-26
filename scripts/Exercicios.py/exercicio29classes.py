class Alunos:

    def __init__(self, nome, RA):
        self.nome = nome
        self.notas = []
        self.ra = RA
        self.media = 0

    def adicionar_notas(self, nota):
        return self.notas.append(nota)
    
    def calcular_media(self):
        for i in self.notas:
            self.media += i 
        
        self.media = self.media / len(self.notas)
        print(f"O aluno {self.nome} tem uma media de: {self.media}")


aluno1 = Alunos("Derek", 333)
aluno2 = Alunos("vitoria", 4444)
aluno3 = Alunos("arroz", 333)
aluno4 = Alunos("batata", 555)
aluno5 = Alunos("pao doce", 111)
