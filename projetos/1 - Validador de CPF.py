# 1 - Validador de CPF se é válido (matematicamente).

"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""


cpf = str(input('Digite o CPF: [Obrigatório escrever "-" para separar o digito] '))

# Leitura, Limpeza e classificação de entrada.
digitos = cpf.split('-')
calc = list()
digito_verificador = list()
for i in digitos[0]:
    if i == '.' or i == '-':
        pass
    else:
        calc.append(int(i))
for i in digitos[1]:
    digito_verificador.append(int(i))


# Cálculo.
cont = soma1 = soma2 = 0

for i in range(10, 1, -1):
    soma1 += (i * calc[cont])
    cont += 1
calc.append(int(digitos[1][0]))
cont = 0
for i in range(11, 1, -1):
    soma2 += (i * calc[cont])
    cont += 1
vf1 = (soma1 % 11)
vf2 = (soma2 % 11)


# Verificando Se é Válido ou Inválido.


def verificador(vf):
    if vf == 0:
        pass
    else:
        vf -= 11
    return abs(vf)

if sum(calc)/len(calc) == calc[0]:
    print('Você digitou uma sequência é Inválido.')
else:
    if verificador(vf1) == digito_verificador[0] and verificador(vf2) == digito_verificador[1]:
        print('Válido')
    else:
        print('Inválido')


# OBS. É interessante criar uma Função, que leia o CPF do usuário de qualquer forma (pontos, traços, com ou sem),
# retornando os valores separados do dígito verificador.

