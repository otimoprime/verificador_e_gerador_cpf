import random

class CPF:
    @staticmethod
    def verificador_cpf(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11:
            return 'O CPF contém 11 digitos. Tente novamente.'
        if cpf == cpf[0] * len(cpf):
            return f'{cpf} não é valido por que são numeros repetidos.'
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito_dez = soma % 11
        digito_dez = 0 if digito_dez < 2 else 11 - digito_dez

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito_onze = soma % 11
        digito_onze = 0 if digito_onze < 2 else 11 - digito_onze

        if cpf[-2:] == f'{digito_dez}{digito_onze}':
            return f'{CPF.cpf_formatar(cpf)} é um CPF válido'
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
        return f'{CPF.cpf_formatar(cpf)}' if cpf_formatado else cpf

    def cpf_formatar(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'

print(f'{'-' * 8} Gerador e Verificador de CPF {'-' * 8}')
while True:

    entrada = input(str('1 - Gerar um CPF aleatório\n2 - Validar um CPF\n3 - Sair\nDigite um número: '))

    if entrada == '1':
        cpf = CPF.gerador_cpf()
        print()
        print(f'CPF aleatório gerado: {cpf}')
        print()
        validar_gerado = input(f'Gostaria de verificar se este CPF é valido? (S/N): ')
        if validar_gerado in ['S', 's']:
            print()
            print(CPF.verificador_cpf(cpf))
            print()
        elif validar_gerado in ['N', 'n']:
            continue
    elif entrada == '2':
        cpf = input(str('Digite o CPF. (Apenas números): '))
        print()
        print(CPF.verificador_cpf(cpf))
        print()
    elif entrada == '3':
        break





