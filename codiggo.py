import random

def verificador_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * len(cpf):
        return f'{cpf} não é valido por que são numeros repetidos.'
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_dez = soma % 11
    digito_dez = 0 if digito_dez < 2 else 11 - digito_dez

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_onze = soma % 11
    digito_onze = 0 if digito_onze < 2 else 11 - digito_onze

    if cpf[-2:] == f'{digito_dez}{digito_onze}':
        return f'{cpf} é um CPF válido'
    else:
        return f'{cpf} não é um CPF válido'
    
def gerador_cpf(cpf_formatado=True):
    numeros = [random.randint(0,9) for _ in range(9)]
    soma = sum(numeros[i] * (10 - i) for i in range(9))
    digito_dez = soma % 11
    digito_dez = 0 if digito_dez < 2 else 11 - digito_dez
    numeros.append(digito_dez)
    
    soma = sum(numeros[i] * (11 - i) for i in range(10))
    digito_onze = soma % 11
    digito_onze = 0 if digito_onze < 2 else 11 - digito_onze
    numeros.append(digito_onze)
    cpf = ''.join(map(str, numeros))

    if cpf_formatado:
        return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
    else:
        return cpf
             
 
alahu = gerador_cpf()
print(alahu)
print(verificador_cpf(alahu))

