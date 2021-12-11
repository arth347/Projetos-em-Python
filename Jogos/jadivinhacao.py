
def jogo():
    import random
    import os
    import _Jogos

    os.system("mode con: cols=36 lines=11")

    t = '-----------------------------------'

    print('***********************************')
    print(' Jogo de adivinhação de numero =)')
    print('***********************************')

    dif = 'dif-valida'
    resultado = 0
    numero_de_tentativas = 0
    pontos = 100


    while True:
        if dif == 'dif-nao-valida':
            print(t,'[',dificuldade,'] não é uma dificuldade.\n')
            print('Digite uma dificuldade válida!!')
            print('facil | medio | dificil')
            dificuldade = input('R: ')
            dif = 'dif-agora-valida'
            
        elif dif == 'dif-valida':
            print('você inicia com 100 pontos e\n perde pontos conforme mais\n longe for o chute')
            print('------------------------------------')
            print('qual dificuldade você deseja?')
            print('facil | medio | dificil')
            dificuldade = input('R: ')
            os.system("mode con: cols=36 lines=6")
            dif = 'dif-agora-valida'
        elif dif == 'dif-agora-valida':
            dif = 'dif-valida'
            if dificuldade == 'facil':
                print(t)
                print('dificuldade [facil] Selecionada =) ')
                numero_de_tentativas = numero_de_tentativas + 3
                numero_secreto = random.randrange(1,11)
                print('*Insira um numero entre 1 e 10*')
                break
            elif dificuldade == 'medio':
                print(t)
                print('Dificuldade [medio] Selecionada =|')
                numero_de_tentativas = numero_de_tentativas + 5
                numero_secreto = random.randrange(1,21)
                print('*Insira um numero entre 1 e 20*')
                break
            elif dificuldade == 'dificil':
                print(t)
                print('Dificuldade [dificil] Selecionada =(')
                numero_de_tentativas = numero_de_tentativas + 10
                numero_secreto = random.randrange(1,101)
                print('*Insira um numero entre 1 e 100*')
                break
            elif dificuldade == 'facil-cheat':
                print(t)
                print('dificuldade [facil-cheat] Selecionada =) ')
                numero_de_tentativas = numero_de_tentativas + 3
                numero_secreto = random.randrange(1,11)
                print('*Insira um numero entre 1 e 10*')
                print('Cheat: [',numero_secreto,']')
                break
                
            elif dificuldade == 'medio-cheat':
                print(t)
                print('Dificuldade [medio-cheat] Selecionada =|')
                numero_de_tentativas = numero_de_tentativas + 5
                numero_secreto = random.randrange(1,21)
                print('*Insira um numero entre 1 e 20*')
                print('Cheat: [',numero_secreto,']')
                break
            elif dificuldade == 'dificil-cheat':
                print(t)
                print('Dificuldade [dificil-cheat] Selecionada =(')
                numero_de_tentativas = numero_de_tentativas + 10
                numero_secreto = random.randrange(1,101)
                print('*Insira um numero entre 1 e 100*')
                print('Cheat: [',numero_secreto,']')
                break
            elif dificuldade == 'IMPOSSIVEL':
                print(t)
                print('Dificuldade ![IMPOSSIVEL]! Selecionada \n( boa sorte >=D )')
                numero_de_tentativas = numero_de_tentativas + 1
                numero_secreto = random.randrange(1,10001)
                print('*Insira um numero entre 1 e 10 000*')
                break
            else:
                dif = 'dif-nao-valida'
                continue

    for rodada in range(1,numero_de_tentativas + 1):
        print(t)
        print('Tentativa',rodada,'de',numero_de_tentativas)
        chute = int(input('Chute um número: '))
        print(t)

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
                print('*Seu numero é maior*')
                
            else:
                print('*Seu numero é menor*')
                
    if resultado == 'ganhou':
        print('-----------------------------------')
        print('       Você fez',pontos,'pontos!')
        print('     Fim, obrigado por jogar =D\n\n')
    else:
        print('-----------------------------------')
        print('       Você fez',pontos,'pontos!')
        print('\n     suas tentativas acabaram, \n         Fim de jogo ;-;\n')
        

    voltar = input('  --> aperte [Enter] para sair <--')
    if voltar == '':
            _Jogos.jogos()
    else:
            _Jogos.jogos()

if(__name__ == '__main__'):
    jogo()

