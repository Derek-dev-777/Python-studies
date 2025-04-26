# exercicio anagramas

def achar_anagrama(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

print(achar_anagrama("python", "java"))
print(achar_anagrama("roma", "amor"))