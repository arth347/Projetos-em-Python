
def jogo():
    import random
    import os

    os.system("mode con: cols=36 lines=40")

    print('***********************************')
    print(' Jogo de adivinhação de numero =)')
    print('***********************************')

    resultado = 0
    numero_de_tentativas = 0
    pontos = 100


    while True:
        print('você inicia com 100 pontos e\n perde pontos conforme mais\n longe for o chute')
        print('------------------------------------')
        print('qual dificuldade você deseja?')
        print('facil | medio | dificil')
        dificuldade = input('R: ')

        if dificuldade == 'facil':
            print('------------------------------------')
            print('dificuldade facil Selecionada =) ')
            numero_de_tentativas = numero_de_tentativas + 3
            numero_secreto = random.randrange(1,11)
            print('*Insira um numero entre 1 e 10*')
            break
        elif dificuldade == 'medio':
            print('------------------------------------')
            print('Dificuldade media Selecionada =|')
            numero_de_tentativas = numero_de_tentativas + 5
            numero_secreto = random.randrange(1,21)
            print('*Insira um numero entre 1 e 20*')
            break
        elif dificuldade == 'dificil':
            print('------------------------------------')
            print('Dificuldade dificil Selecionada (=(')
            numero_de_tentativas = numero_de_tentativas + 10
            numero_secreto = random.randrange(1,101)
            print('*Insira um numero entre 1 e 100*')
            break
        elif dificuldade == 'facil-cheat':
            print('------------------------------------')
            print('dificuldade facil Selecionada =) ')
            numero_de_tentativas = numero_de_tentativas + 3
            numero_secreto = random.randrange(1,11)
            print('*Insira um numero entre 1 e 10*')
            print('Cheat: [',numero_secreto,']')
            break
            
        elif dificuldade == 'medio-cheat':
            print('------------------------------------')
            print('Dificuldade media Selecionada =|')
            numero_de_tentativas = numero_de_tentativas + 5
            numero_secreto = random.randrange(1,21)
            print('*Insira um numero entre 1 e 20*')
            print('Cheat: [',numero_secreto,']')
            break
        elif dificuldade == 'dificil-cheat':
            print('------------------------------------')
            print('Dificuldade dificil Selecionada (=(')
            numero_de_tentativas = numero_de_tentativas + 10
            numero_secreto = random.randrange(1,101)
            print('*Insira um numero entre 1 e 100*')
            print('Cheat: [',numero_secreto,']')
            break
        elif dificuldade == 'IMPOSSIVEL':
            print('------------------------------------')
            print('Dificuldade !-IMPOSSIVEL-! Selecionada \n( boa sorte >=D )')
            numero_de_tentativas = numero_de_tentativas + 1
            numero_secreto = random.randrange(1,10001)
            print('*Insira um numero entre 1 e 10 000*')
            break
        else:
            print('digite uma dificuldade válida:')
            continue

    for rodada in range(1,numero_de_tentativas + 1):
        print('------------------------------------')
        print('Tentativa',rodada,'de',numero_de_tentativas)
        chute = int(input('Chute um número: '))
        print('------------------------------------')

        if dificuldade == 'facil' or dificuldade == 'facil-cheat':
            if chute < 1 or chute > 10:
                print('***********************************')
                print('Você deve inserir um \nnumero entre 1 e 10!')
                print('- 1 Tentativa >=(')
                print('***********************************')
                continue
        elif dificuldade == 'medio' or dificuldade == 'medio-cheat':
            if chute < 1 or chute > 20:
                print('***********************************')
                print('Você deve inserir um \nnumero entre 1 e 20!')
                print('- 1 Tentativa >=(')
                print('***********************************')
                continue
        elif dificuldade == 'dificil' or dificuldade == 'dificil-cheat':
            if chute < 1 or chute > 100:
                print('***********************************')
                print('Você deve inserir um \nnumero entre 1 e 100!')
                print('- 1 Tentativa >=(')
                print('***********************************')
                continue
        elif dificuldade == 'IMPOSSIVEL':
            if chute < 1 or chute > 10000:
                print('***********************************')
                print('Você deve inserir um \nnumero entre 1 e 100!')
                print('Se fudeo troxa perdeu a sua unica chance burro do carai kkkk')
                print('***********************************')
                continue
            
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

        if acertou:
            print('Você digitou',chute,'e acertou! =D')
            resultado = 'ganhou'
            break
        else:
            print('Você digitou',chute,'e errou. =(')
            resultado = 'perdeu'
            if maior:
                print('*Seu numero é maior do que o numero secreto')
                
            else:
                print('*Seu numero é menor do que o numero secreto')
                
    if resultado == 'ganhou':
        print('-----------------------------------')
        print('Você fez',pontos,'pontos!')
        print('Fim, obrigado por jogar =D')
        input('--> aperte enter para sair <--')
    else:
        print('-----------------------------------')
        print('Você fez',pontos,'pontos!')
        print('que pena, suas \ntentativas acabaram, \nFim de jogo ;-;')
        input('--> aperte enter para sair <--')