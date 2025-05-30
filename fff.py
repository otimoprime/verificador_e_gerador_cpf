import random

def gerador_cpf(cpf_formatado=True):
    numeros = [5,4,3,6,5,4,6,7,6]
    soma = sum(n * (10 - i) for i, n in enumerate(numeros))
    digito_dez = soma % 11
    digito_dez = 0 if digito_dez < 2 else 11 - digito_dez
    numeros.append(digito_dez)
        # Calcula o segundo dígito verificador
    soma = sum(n * (11 - i) for i, n in enumerate(numeros))
    digito2 = (soma * 10) % 11
    digito2 = 0 if digito2 >= 10 else digito2
    numeros.append(digito2)
    return numeros

alahu = gerador_cpf()
print(alahu)

def gerador_cpf(cpf_formatado=True):
    numeros = [5,4,3,6,5,4,6,7,6]
    soma = sum(n * (10 - i) for i, n in enumerate(numeros))
    digito_dez = soma % 11
    digito_dez = 0 if digito_dez < 2 else 11 - digito_dez 
    numeros.append(digito_dez)

    soma = sum(numeros[0] * (11 - i) for i in range(10))
    digito_onze = soma % 11
    digito_onze = 0 if digito_onze < 2 else 11 - digito_onze
    numeros.append(digito_onze)
    return numeros
alahu = gerador_cpf()
print(alahu)