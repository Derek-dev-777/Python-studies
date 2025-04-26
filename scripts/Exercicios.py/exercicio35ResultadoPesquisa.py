
meu_dict = {}

votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

for voto in votos:
    if voto in meu_dict:
        meu_dict[voto] += 1
    else:
        meu_dict[voto] = 1


print(meu_dict)