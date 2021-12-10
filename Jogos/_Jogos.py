def jogos():
    import os
    import jadivinhacao
    import jforca

    os.system("mode con:cols=36 lines=40")

    print('***********************************')
    print('         Jogos em python')
    print('           By:Arth347')
    print('***********************************')

    while True:
        print('| adivinhacao | forca |')
        print('***********************************')
        jogo = input('Selecione o jogo:\nR:')

        if jogo == 'adivinhacao':
            print('***********************************')
            print('------------------------------------')
            print('Jogo Selecionado com Sucesso!')
            print('------------------------------------')
            jadivinhacao.jogo()
            break
        elif jogo == 'forca':
            print('***********************************')
            print('------------------------------------')
            print('Jogo Selecionado com Sucesso!')
            print('------------------------------------')
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