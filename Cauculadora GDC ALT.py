print('Calculadora de dois números')

while True:
 dig1 = int(input('Digite o primeiro número:\nResposta: '))
 dig2 = int(input('Digite o segundo número:\nResposta: '))
 escolha = input('Escolha a operação: \n Soma,\n Subtração,\n Multiplicação, \n Divisão \n(digite como escrito acima)\nResposta:')
 if escolha == 'Soma' :
  print('A soma é igual à:',dig1 + dig2)
  rsp =input('quer fazer outra conta? \n(sim/não)\nResposta:')
  if rsp == 'não':
    print('ok encerrando...')
    break
  else:
    print('ok iniciando...')
 elif escolha == 'Subtração':
  print('A diferença é igual à:',dig1 - dig2)
  rsp =input('quer fazer outra conta? \n(sim/não)\nResposta:')
  if rsp == 'não':
    print('ok encerrando...')
    break
  else:
    print('ok iniciando...')
 elif escolha == 'Multiplicação':
  print('O produto é igual à:',dig1 * dig2)
  rsp =input('quer fazer outra conta? \n(sim/não)\nResposta:')
  if rsp == 'não':
    print('ok encerrando...')
    break
  else:
    print('ok iniciando...')
 elif escolha == 'Divisão':
  print('O quociente é igual à:',dig1 / dig2)
  rsp =input('quer fazer outra conta? \n(sim/não)\nResposta:')
  if rsp == 'não':
    print('ok encerrando...')
    break
  else:
    print('ok iniciando...')
 else:
  print('Porra escreve certo')
 
  
  