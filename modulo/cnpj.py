def apenasnumeros_cnpj(cnpj):
    novo_cnpj = list()
    for item in cnpj:
        if item == '-':
            break
        if item.isnumeric():
            novo_cnpj.append(int(item))

    return novo_cnpj


def verificador_dig_1(cnpj):
    verificador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cont = 0
    resultados = list()
    for item in cnpj:
        c = verificador[cont] * item
        cont += 1
        resultados.append(c)

    digito = 11 - (sum(resultados) % 11)
    if digito >= 10:
        digito = 0
    return digito


def verificador_dig_2(cnpj):
    i = verificador_dig_1(cnpj)
    cnpj.append(i)
    verificador = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cont = 0
    resultados = list()
    for item in cnpj:
        c = verificador[cont] * item
        cont += 1
        resultados.append(c)

    digito = 11 - (sum(resultados) % 11)
    if digito >= 10:
        digito = 0
    return digito


def extrair_digitos(cnpj):

    return cnpj[-2:]
