import random
class CPF:
    @staticmethod
    def verificador_cpf(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11:
            return 'O CPF contém 11 digitos. Tente novamente.'
        if cpf == cpf[0] * len(cpf):
            return f'{cpf} não é valido por que são numeros repetidos.'
        digitos_gerados = CPF.gerar_ultimos_digitos(numeros=False, cpf=cpf[:-2])
        if cpf[-2:] == f'{digitos_gerados[-2]}{digitos_gerados[-1]}':
            return f'{CPF.cpf_formatar(cpf)} é um CPF válido'
        else:   
            return f'{CPF.cpf_formatar(cpf)} não é um CPF válido'
    def gerar_ultimos_digitos(numeros=False, cpf=None):
        if numeros:
            numeros = [random.randint(0,9) for _ in range(9)]
        else: 
            numeros = [int(d) for d in cpf]
        soma = sum(int(numeros[i]) * (10 - i) for i in range(9))
        digito_dez = soma % 11
        digito_dez = 0 if digito_dez < 2 else 11 - digito_dez
        numeros.append(digito_dez)

        soma = sum(int(numeros[i]) * (11 - i) for i in range(10))
        digito_onze = soma % 11
        digito_onze = 0 if digito_onze < 2 else 11 - digito_onze
        numeros.append(digito_onze)
        return numeros
    def gerador_cpf(cpf_formatado=True):
        numeros = CPF.gerar_ultimos_digitos(numeros=True)
        numeros = ''.join(map(str, numeros))   
        return f'{CPF.cpf_formatar(numeros)}' if cpf_formatado else cpf
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





