def jogo():

    import os

    os.system("mode con: cols=36 lines=10")

    print('***********************************')
    print('   Bem vindo ao jogo da Forca!')
    print('***********************************')

    palavra_secreta = 'shrek'
    enforcado = False
    acertou = False
    posicao = 0
    erros = 0
    letras_acertadas = [ '_' for letra in palavra_secreta]

    print('Erros:')
    print('\n\n')
    print('-----------------------------------')
    while enforcado == False and acertou == False:
        print('Digite uma letra: \n\n',letras_acertadas)
        chute = str(input('\nR:').strip().lower())
        if erros == 0:
            print('Erros:')
            print('\n\n')
            print('-----------------------------------')

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra.upper()
                posicao = posicao + 1
        else:
            print('Você errou uma letra!')
            erros = erros + 1
            if erros == 1:
                print('Erros:')
                print('  O  ')
                print('     ')
                print('     ')
            elif erros == 2:
                print('Erros:')
                print('  O  ')
                print('  |  ')
                print('     ')
            elif erros == 3:
                print('Erros:')
                print('  O  ')
                print(' /|  ')
                print('     ') 
            elif erros == 4:
                print('Erros:')
                print('  O  ')
                print(' /|\ ')
                print('     ')
            elif erros == 5:  
                 print('Erros:')
                 print('  O  ')
                 print(' /|\ ')
                 print(' /   ')
            elif erros == 6:
                print('Erros:')
                print('  O  ')
                print(' /|\     Você Foi enforcado!!')
                print(' / \ ')
            print('-----------------------------------')

        acertou = '_' not in letras_acertadas
        enforcado = erros == 6  
        posicao = posicao * 0 
    if acertou == True: 
        print(letras_acertadas,'\nVocê acertou!')
    else:
        print('Você foi enforcado e perdeu ;-;')
    input('--> aperte enter para sair <--')

if(__name__ == '__main__'):
    jogo()