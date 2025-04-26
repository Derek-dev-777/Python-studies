primeirovalor = int(input("Digite um valor: "))
segundovalor = int(input("Digite outro valor: "))

if primeirovalor > segundovalor:
    print(f"o primeiro valor ({primeirovalor}) é maior do que o segundo valor ({segundovalor})")

elif segundovalor > primeirovalor:
    print(f"o segundo valor ({segundovalor}) é maior do que o primeiro valor ({primeirovalor})")
    
elif primeirovalor == segundovalor:
    print(f"Os dois valores são iguais.")
