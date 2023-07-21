from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print(''' Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print('-='*11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)

print('-='*11)
print('O Computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0:#computador jogou pedra
    if jogador == 0:
        print('EMPATE')
        
    elif jogador == 1:
        print('JOGADOR VENCE')
        
    elif jogador == 2:
        print('COMPUTADOR VENCE')
        
    else:
        print('JOGADA INVÁLIDA!')
        
elif computador == 1:#computador jogou papel
    
    if jogador == 0:
        print('COMPUTADOR VENCE')
        
    elif jogador == 1:
        print('EMPATE')
        
    elif jogador == 2:
        print('JOGADOR VENCE')
        
    else:
        print('JOGADA INVÁLIDA!')
        
elif computador == 2:#computador jogou tesoura
    
    if jogador == 0:
        print('JOGADOR VENCE')
        
    elif jogador == 1:
        print('COMPUTADOR VENCE')
        
    elif jogador == 2:
        print('EMPATE')
        
    else:
        print('JOGADA INVÁLIDA!')
