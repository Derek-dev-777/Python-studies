
cpf = '52748373871'
nove_digitos = cpf[:9]
dez_digitos = cpf [:10]
contador_regressivo = 10
contador_regressivo2 = 11
resultado = 0
resultado2 = 0

for numero in nove_digitos:
    resultado += int(numero)*contador_regressivo
    contador_regressivo -= 1

    primeiro_digito = resultado * 10
    primeiro_digito = primeiro_digito % 11
if primeiro_digito > 9:
    primeiro_digito = 0
    print(f"o primeiro digito do seu cpf é {primeiro_digito}")
else:
    print(f"o primeiro digito do seu cpf é {primeiro_digito}")

for numero2 in dez_digitos:
    resultado2 += int(numero2) * contador_regressivo2
    contador_regressivo2 -= 1

    segundo_digito = resultado2 * 10
    segundo_digito = segundo_digito % 11
if segundo_digito > 9:
    segundo_digito = 0
    print(f"o segundo digito do seu cpf é {segundo_digito}")
else:
    print(f"o segundo digito do seu cpf é {segundo_digito}")

cpf_gerado_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == cpf_gerado_calculo:
    print(f"{cpf} é valido")
else:
    print("CPF invalido.")