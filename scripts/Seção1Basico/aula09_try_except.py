# try -> tentar executar o codigo
# except -> ocorreu algum erro ao tentar executar

numero = (input("Vou dobrar o numero que você digitar: "))


try:
    numero_int = int(numero)
    print(f"o dobro de {numero} é igual a: {numero_int * 2}")

except:
    print(" Isso não é um numero")


# esse codigo evita com que digitem string onde devem digitar digitos ou algo do tipo