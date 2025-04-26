from threading import Thread
from time import sleep

class MeuThread(Thread):
    def __init__(self, Tempo, Texto):
        self.tempo = Tempo
        self.texto = Texto

        super().__init__()

        def run(self):
            sleep(self.tempo)
            print(self.texto)
            