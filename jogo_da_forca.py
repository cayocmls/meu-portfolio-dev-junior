import os

print('=-='*7)
print('   JOGO DA FORCA')
print('=-='*7)


palavra_secreta = 'perfume'
letras_acertadas = '' #para saber quantas letras foram acertadas pelo usuário.
n_tentativas = 0 #contagem de tentativas.

while True:

    letra_digitada = input('Digite uma letra: ')
    n_tentativas += 1 #efetuar somatório de tentativas.
    
    if len(letra_digitada) > 1: #caso o usuário digite mais de uma letra, reiniciará o loop.
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta: #saber se a letra digitada está na palavra escolhida.
        letras_acertadas += letra_digitada #concatenar a letra digitada quando contida na palavra escolhida.
    
    palavra_formada = '' # transformar a formatação vertical em horizontal.
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas: #se a letra escolhida estiver contida na palavra escolhida, exibe a letra.
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*' #se a letra não estiver contida na palavra, exibe *
    
    print('Palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!  PARABÉNS!!')
        print('A palavra era: ', palavra_formada)
        print('Tentativas: ', n_tentativas)
        letras_acertadas = '' #zerar os contadores.
        n_tentativas = 0 #zerar os contadores.
