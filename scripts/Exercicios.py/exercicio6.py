# fahrenheit para celsius
def converter(x):
    return 5 * ((x-32) / 9)

while True:
    faren = input("Digite a temperatura em fahrenheit: ")
    try:
        faren = float(faren)
        temperatura = converter(faren)
        print(f"A temperatura em celsius é {temperatura:.2f}")
    except ValueError:
        print("error, algo aconteceu tente novamente")