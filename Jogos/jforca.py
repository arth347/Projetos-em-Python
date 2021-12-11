def jogo():
    
    #VARIAVEIS
    enforcado = False
    acertou = False
    posicao = 0
    erros = 0
    t = '-----------------------------------'

    # FORCA
    erro0 = 'Erros:\n\n\n'
    erro1 = 'Erros:\n  O  \n         Você errou uma letra!\n   '
    erro2 = 'Erros:\n  O  \n  |      Você errou uma letra!\n   '
    erro3 = 'Erros:\n  O  \n /|      Você errou uma letra!\n   '
    erro4 = 'Erros:\n  O  \n /|\     Você errou uma letra!\n   '
    erro5 = 'Erros:\n  O  \n /|\     Você errou uma letra!\n / '
    erro6 = 'Erros:\n  O  \n /|\     Você Foi enforcado!!\n / \ '

    mude_o_tamanho_da_janela_para_36x10()

    diga_mensagem_inicial(erro0,t)
    
    palavra_secreta = sorteie_palavra_secreta()
    
    letras_secretas = transforme_palavra_secreta_em_letras_secretas(palavra_secreta)

    while enforcado == False and acertou == False:
        chute = pede_o_chute(letras_secretas)

        if erros == 0:
           print(erro0)
           print(t)
        elif erros == 1:
            print(erro1)
            print(t)
        elif erros == 2:
            print(erro2)
            print(t)
        elif erros == 3:
            print(erro3)
            print(t)
        elif erros == 4:
            print(erro4)
            print(t)
        elif erros == 5:  
            print(erro5)
            print(t)
        elif erros == 6:
            print(erro6)
            print(t)
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_secretas[posicao] = letra.upper()
                posicao += 1
        else:
            print('\n')
            erros = erros + 1
            
            if erros == 1:
                print(erro1)
                print(t)
            elif erros == 2:
                print(erro2)
                print(t)
            elif erros == 3:
                print(erro3)
                print(t)
            elif erros == 4:
                print(erro4)
                print(t)
            elif erros == 5:  
                print(erro5)
                print(t)
            elif erros == 6:
                print(erro6)
                print(t)
               
        acertou = '_' not in letras_secretas
        enforcado = erros == 6  
        posicao *= 0 
    if acertou == True: 
        print('         Você Ganhou !!! \n\n       a palavra era:',palavra_secreta,'\n')
        if palavra_secreta == 'shrek':
            inverta_a_cor_do_cmd()
            mude_o_tamanho_da_janela_para_caber_o_shrek()
            shrek = open('shrek-imagem2.txt','r')
            contagem = 0
            linhas = []


            for linha in shrek:
                linha = linha.strip()
                linhas.append(linha)
            shrek.close()

            while True:
                shrek_img = linhas[contagem]
                print(shrek_img)
                contagem += 1
                if contagem < 42:
                    continue
                else:
                    break

            print('=========================================================================================================================================================================================================')
            print('=                                                                                            Você Ganhou !!!                                                                                            =')
            print('=                                                                                      a palavra era: [shrek]                                                                                           =')
            print('=========================================================================================================================================================================================================')
        elif palavra_secreta == 'gigiodc':
            inverta_a_cor_do_cmd()
            mude_o_tamanho_da_janela_para_caber_gigiodc()
            gigi = open('gigi.txt','r')
            contagem = 0
            linhas = []


            for linha in gigi:
                linha = linha.strip()
                linhas.append(linha)
            gigi.close()

            while True:
                gigi_img = linhas[contagem]
                print(gigi_img)
                contagem += 1
                if contagem < 91:
                    continue
                else:
                    break

            print('=========================================================================================================================================================================================================')
            print('=                                                                                            Você Ganhou !!!                                                                                            =')
            print('=                                                                                      a palavra era: [gigiodc]                                                                                         =')
            print('=========================================================================================================================================================================================================')
            
        
            
    else:
        print('   Você foi enforcado e perdeu ;-; \n\n       a palavra era:',palavra_secreta,'\n')
       
    apresente_a_opcao_de_sair()



# FUNÇÕES

# ESSA FUNÇÃO MUDA O TAMANHO DA JANELA PARA 36X10
def mude_o_tamanho_da_janela_para_36x10():
    import os
    
    os.system("mode con: cols=36 lines=10")

#  ESSA FUNÇÃO MOSTRA A MENSAGEM INICIAL
def diga_mensagem_inicial(erro0,t):
    print('***********************************')
    print('   Bem vindo ao jogo da Forca!')
    print('***********************************')
    input('\n\n-->Aperte [Enter] para começar<--')
    print('\n')
    print(erro0)
    print(t)

#  ESSA FUNÇÃO SORTEIA ALGUMA PALAVRA DO ARQUIVO: jforca-palavras.txt
def sorteie_palavra_secreta():
    import random 
    forca_rsp = open('jforca-palavras.txt','r')

    palavras = []
    for linha in forca_rsp:
        linha = linha.strip()
        palavras.append(linha)

    forca_rsp.close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero]

    return palavra_secreta

#  ESSA FUNÇÃO ESCONDE AS LETRAS DA PALAVRA SECRETA
def transforme_palavra_secreta_em_letras_secretas(palavra_secreta):
     return  [ '_' for letra in palavra_secreta]

#  ESSA FUNÇÃO PEDE O CHUTE
def pede_o_chute(letras_secretas):
    print('Digite uma letra: \n\n',letras_secretas)
    chute = str(input('\nR:').strip().lower())
    return chute 

# ESSA FUNÇÃO APRESENTA A OPSÃO DE SAIR
def apresente_a_opcao_de_sair():
    import _Jogos

    voltar = input('  --> aperte [Enter] para sair <--')
    if voltar == '':
        _Jogos.jogos()
    else:
        _Jogos.jogos()

#ESSA FUNÇÃO ALMENTA A JANELA PARA CABER O SHREK
def mude_o_tamanho_da_janela_para_caber_o_shrek():
    import os
    os.system("mode con: cols=201 lines=47")
#ESSA FUNÇÃO DEIXA O CMD COM A COR INVERTIDA
def inverta_a_cor_do_cmd():
    import os
    os.system('color f0')
#ESSA FUNÇÃO ALMENTA A JANELA PRA CABER O NEGOCIO GRANDE DO GIGIODC
def mude_o_tamanho_da_janela_para_caber_gigiodc():
    import os
    os.system('mode con: cols=201 lines=94')

#  FIM
if(__name__ == '__main__'):
    jogo()



