
string = "banana"
meu_dict = {}

for letras in string:
    print(letras)
    if letras in meu_dict:
        meu_dict[letras] += 1
    else:
        meu_dict[letras] = 1

print(meu_dict)
    