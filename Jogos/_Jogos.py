def jogos():
    import os
    import jadivinhacao
    import jforca

    os.system('color 0f')

    t = '-----------------------------------'

    os.system("mode con:cols=36 lines=9")

    print('***********************************')
    print('         Jogos em python')
    print('           By:Arth347')
    print('***********************************')

    while True:
        print('| adivinhacao | forca |')
        print('***********************************')
        jogo = input('Selecione o jogo:\nR:')
        print(t)

        if jogo == 'adivinhacao':
            jadivinhacao.jogo()
            break
        elif jogo == 'forca':
            
            jforca.jogo()
            break
        else:
            print('***********************************')
            print('------------------------------------')
            print('Desculpe mas esse jogo não existe.\nPor favor digite novamente:')
            print('------------------------------------')
            print('***********************************')
            continue
if(__name__ == '__main__'):
    jogos()