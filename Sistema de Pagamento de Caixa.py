import datetime

preco=float(input('\nPreço da compras: R$ '))
print('''
*****************************
     FORMAS DE PAGAMENTO
*****************************

[1] à vista dinheiro Desconto de 10%
[2] à vista cartão  Desconto de 5%
[3] 2x no cartão  Juros 10%
[4] Mais X no Cartão  Juros 20% + 1% Mes''')
opcao=int(input('\nQual é a opção? '))
print('\n*****************************')

if opcao==1:
    desconto=preco-(preco*10/100)
    print('\nSua compra vai ter 10% de desconto!')
    print('\nDe R$ {:.2f} caiu para R$ {:.2f}!\n'.format(preco,desconto))

elif opcao==2:
    desconto=preco-(preco*5/100)
    print('\nSua compra vai ter 5% de desconto!')
    print('\nDe R$ {:.2f} foi para R${:.2f}!\n'.format(preco,desconto))

elif opcao==3:

    juros=preco+(preco*10/100)

    print('\nParcelado em até 2x...')
    print('\nValor a Pagar C/ Juros de 10%  R$ {:.2f}\n'.format(juros))


    from datetime import datetime, timedelta

    data_atual = datetime.now()
    prox_mes = data_atual + timedelta(days=(30*(2)))
    mes_proximo = prox_mes.strftime("%B de %Y")
   
    PorMes = juros/2
    print(f"Voce vai pagar Por Mes R$ {PorMes}")
    print("Voce vai Pagar até :", mes_proximo)
    print()

elif opcao==4:
    print("\n20% de Juros + 1% Mes")
    parcelas = int(input('\nQuantas parcelas serão ? '))

    juros=preco+(preco*(20+parcelas)/100)

    from datetime import datetime, timedelta

    data_atual = datetime.now()
    prox_mes = data_atual + timedelta(days=(30*(parcelas)))
    mes_proximo = prox_mes.strftime("%B de %Y")

    print('\nSua compra vai custar R$ {:.2f}  C/ Juros de 20% + 1% Juros\n'.format(juros))
    
    PorMes=juros/parcelas
    print(f"por mes voce vai pagar: R$: {PorMes}")

    print("Voce vai Pagar até :", mes_proximo)
    print()
else:
    print('\nNúmero inválido!')