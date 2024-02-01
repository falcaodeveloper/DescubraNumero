from random import randint
from time import sleep
import pygame

mensagem = '''Vamos jogar! Você digitará um número entre 0 à 5 e vou escolher um número também nesse mesmo intervalo.
Se o número escolhido por você for igual ao que escolhi, você ganha 1 ponto caso contrário eu ganho 1 ponto.\n'''

x = '=' * 80
voce = 'Você: {} ponto(s)'
python = 'Computador: {} ponto(s)\n'
pensando = '\nUm momento! Estou pensando em um número...\n'
sairJogo = 'Se quiser sair do jogo, não digite nada e tecle "ENTER".\n'

usuario = 0
computador = 0
continuar = ""

print(x)
print(mensagem)
print(x)
while continuar == '':
    resposta = (input('Digite um número:'))
    valorLogico = resposta.isnumeric()
    match valorLogico:
        case False:
            print('Você saiu do jogo.')
            break
        case _:
            resposta = int(resposta)
            print(pensando)
            pygame.mixer.init()
            pygame.mixer.music.load('music/ambient-piano-logo-165357.mp3')#https://pixabay.com/sound-effects/ambient-piano-logo-165357/           
            pygame.mixer.music.play()
            sleep(5)
            valor = randint(0, 5)
            if valor == resposta:
                print('Você ganhou um ponto, pois pensei no número {}' .format(valor))
                usuario += 1
                print(voce.format(usuario))
                print(python.format(computador))
            else:
                print('Você se deu mal! Bem feito, hahahahahaha. Pensei no número {}' .format(valor))
                print(voce.format(usuario))
                computador += 1
                print(python.format(computador))
            print(sairJogo)
            print(x)