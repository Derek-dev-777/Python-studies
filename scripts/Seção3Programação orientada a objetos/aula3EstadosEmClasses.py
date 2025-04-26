
class Camera():
    def __init__(self, name, recording=False ):
        self.name = name
        self.recording = recording
    

    def filmando(self):

        print(f"{self.name} está filmando...")
        self.recording = True

    def parar_filmando(self):

        print(f"{self.name} estou parando de filmar")
        self.recording = False

    def fotografar(self):
        if self.recording:
            print(f"{self.name} está fotografando...")

c1 = Camera("Gopro")
c1.filmando()
c1.fotografar()