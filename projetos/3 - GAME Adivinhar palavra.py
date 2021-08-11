# 3 - GAME Adivinhar Palavra.
from random import choice
from cores import *
from time import sleep

def linha():
    print('-=' * 35)


# Conjunto de palavras para o jogo
palavras = ['azul', 'motocicleta', 'carro', 'automovel', 'gato', 'girafa', 'elefante', 'fruta',
            'laranja', 'banana', 'madeira', 'sorteado', 'espanha', 'unidos', 'sertanejo', 'rock',
            'sonhar', 'correr', 'celular', 'smartphone', 'caneca', 'controle', 'cadeira', 'agasalho'
            ]

palavra_secreta = choice(palavras)  # Seleciona a palavra secreta da partida.
apostas = []  # guarda os palpites do jogador durante a partida.

linha()
print(fundoazulclaro('{:^70}'.format('JOGO ADIVINHE A PALAVRA')))

# Denomina a dificuldade do jogo (relacionado ao número de tentativas erradas).
while True:
    try:
        print(azul('Selecione a dificuldade do jogo:'))
        print(azul('1 -'), verde('Fácil'))
        print(azul('2 -'), amarelo('Médio'))
        print(azul('3 -'), vermelho('Difícil'))
        x = int(input(''))     # Recebe entrada.
    except ValueError:
        print('ops! Escolha usando um número corresponde a dificuldade...')  # Testa se pode ser usado.
    else:
        if x > 4 or x < 0:  # Verifica se é válida para uma dificuldade.
            print('opa! Tente novamente escolhendo entre 1, 2 ou 3...')

        else:  # Define a quantidade de chances de acordo com a dificuldade.
            if x == 1:
                chances = 8
                print(('Você escolheu a dificuldade'), verde('Fácil!'))

                break

            if x == 2:
                chances = 6
                print(('Você escolheu a dificuldade'), amarelo('Média!'))
                break
            if x == 3:
                chances = 4
                print(('Você escolheu a dificuldade'), vermelho('Difícil!'))
                break
print(branco('Vamos iniciar'), end='')
for i in range(0,7):
    print('.', end='', flush=True)
    sleep(0.4)
print()

# Leitura e andamento do jogo.
while True:

    if chances == 0:  # Verifica as chances, quando chegar a 0 o jogador perde a partida.
        print(vermelho(f'Você perdeu!!! A palavra é {ciano(palavra_secreta.upper())}'))
        break

    # Instruções ao jogador.
    linha()
    print(fundoazul('{:^70}'.format('JOGO ADIVINHE A PALAVRA')))
    linha()

    print(branco('Cuidado, digite apenas uma letra\nsó é considerado a primeira letra que você digitar! ok? '))

    while True:  # loop infinito até recerber uma entrada válida que está dentro do alfabeto.
        try:
            letra = str(input(azul('Digite uma letra: '))).strip()[0]
        except IndexError:
            pass
        else:
            if letra in 'abcdefghijklmnopqrstuvwxyz':
                break
            else:
                print('Erro. Não pode ser usado números nem símbolos. Tente Novamente...')

    if letra not in apostas:  # Verifica se a letra da vez já foi apostada.
        apostas.append(letra)

        if letra in palavra_secreta:  # Check se a palavra secrera possui a aposta.
            print(azulnegrito('Parabéns! A letra'), fundoazul(f" {(letra.upper())} "),
                  azulnegrito('está presente na palavra secreta.'))

        else:
            print(vermelho(f'Ops.. Tente novamente! A palavra secreta não possui a letra'),
                  fundovermelho(f' {(letra.upper())} '), vermelho('.'))

        secreto_temp = ''
        for letra_descoberta in palavra_secreta:  # Apresenta a palavra secretra, interagindo com o avanço do jogo.
            if letra_descoberta in apostas:
                secreto_temp += letra_descoberta
            else:
                secreto_temp += '*'

        if secreto_temp == palavra_secreta:  # Se todos elementos da palavra secreta for descoberto,  ganha o jogo.
            print(verde(
                f'Que legal! Você descobriu a palavra secreta! A palavra é'),
                fundoverde(f' {palavra_secreta.upper()} '))
            break
        else:

            linha()
            print()
            print(cinza(f'A palavra secreta é'), brancofundo(f' {secreto_temp.upper()} '))

        if letra not in palavra_secreta:  # Jogador perde uma chance a cada tentativa errada.
            chances -= 1

    else:
        print(amarelo('Você já tentou essa letra.'))
    print(pretofundo(f'Você tem {chances} chances...'))  # Apresenta quantas chances até o final da partida.
    print()