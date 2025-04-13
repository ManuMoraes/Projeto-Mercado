#27/11/2021
soma = 0
decimal_valor = 1
produtos = ''
cupons = 5432,0.95,   6546,0.9,  6545,0.87,   2566,0.82,   8742,0.80,   8523,0.92,   7464,0.93,   2234,0.94
tupla_Produtos = 'açúcar',2.5,'feijão',5.5,'fubá',4,'trigo',4.5,'macarrão',8,'shampoo',8.98,'sabão em pó',9.9,'arroz-2kg',6.25,'alface',1.99,'café',10.99,'sal',1.39,'mortadela',12.99,'cebola',5.9,'papel higiênico',5.49,'mussarela',36.9,'margarina',6.79,'nescau',6.35,'presunto',21.9,'laranja',2.79,'pasta de dente',4.29,'ovos',6.49,'chiclete',0.1,'chocotone',18.9,'panetone',17.9,'uva verde',12.9,'leite em pó',11.99,'biscoito',3.99,'farofa',2.9,'leite',3.7,'apontador',2.1,'cola bastão',2.5,'giz de cera',5.9,'tesoura',6.9,'régua',2.5,'branquinho',1.99,'lápis',1.75,'borracha',2,'caderno',15.9,'estojo',25,'transferidor',4.2,'compasso',9.99,'mochila',120.32,'canetas',22.3,'livro',34.9,
#manual e apresentação
print('{}\n\033[32m            ✨ BEM VINDO  ✨\033[m\n{}'.format('-=-' * 13,'-=-' * 13))
print('{}\n{}\033[35mMANUAL\033[m\n{}'.format('\033[36m--\033[m' * 20,' ' * 15,'\033[36m--\033[m' * 20))
print('Digite \033[33mlista\033[m para ver a lista de preços\nNome do produto para opções\n\033[33mTotal\033[m para ver o valor a pagar até então\n\033[33mCupom\033[m para insirir um cupom de desconto\n(VOCÊ SÓ PODE USAR UM CUPOM POR COMPRA)\nDigite \033[33m0\033[m para finalizar a compra')
print('\033[36m--\033[m' * 20)
while True:
    input_escolha = input('\033[31m').strip().lower()
    if input_escolha == '0':
        break
#exibir lista
    if input_escolha == 'lista':
        print('{}\n{}\033[35mLISTAGEM DE PREÇOS\033[m\n{}'.format('\033[36m--\033[m' * 20,' ' * 10,'\033[36m--\033[m' * 20))
        for c in range (0,len(tupla_Produtos),2):
            lenlista = len(tupla_Produtos[c])
            print('{}{}R$ {:.2f}'.format(tupla_Produtos[c].capitalize(),'.' * (30 - lenlista),tupla_Produtos[c + 1]))
        print('\033[36m--\033[m' * 20)
#código do cupom
    if input_escolha == 'cupom':
        while True:
            codigo = input('\033[mDigite o código do cupom ou [ \033[33mcancel\033[m ] para cancelar:\033[31m\n')
            if codigo.isnumeric() == True:
                codigo = int(codigo)
            else:
                if codigo.strip().lower() == 'cancel':
                    break
            if cupons.count(codigo) != 0:
                indiceCodigo = cupons.index(codigo)
                desconto = 100 - (cupons[indiceCodigo + 1] * 100)
                decimal_valor = cupons[indiceCodigo + 1]
                print(f'\033[mVocê recebeu um desconto de {desconto:.0f}%\033[31m')
                break
            else:
                print('\033[31mCódigo de cupom inválido\033[m')
#testar se o produto existe na lista
    if tupla_Produtos.count(input_escolha) != 0:
        indice = tupla_Produtos.index(input_escolha)
        print(f'\033[mO produto \033[32m{tupla_Produtos[indice].capitalize()}\033[m custa R$ {tupla_Produtos[indice + 1]:.2f}')
#testar se o usuário deseja adicionar este item ao carrinho
        while True:
            s_n = input('\033[mDeseja adicionar este item ao carrinho? [S/N] \033[31m').lower().strip()
            if s_n == 's':
                soma += tupla_Produtos[indice + 1]
                produtos += tupla_Produtos[indice] + '...'
                break
            elif s_n == 'n':
                break
#ver total
    if input_escolha == 'total':
        print(f'\033[mO total a pagar até o momento é R${soma * decimal_valor:.2f}\nNo carrinho estão os produtos:\n{produtos}')
if soma == 0:
    print('\033[33mVocê não comprou nenhum produto!\nNão é necessário efetuar pagamento.\033[m')
else:
    print(f'\033[mTotal bruto: R${soma:.2f}\nDesconto: {100 - (decimal_valor * 100):.0f}%')
    total = soma * decimal_valor
    print('\033[33mTotal{}R$ {:.2f}\033[m'.format('.' * (30 - 5),total))
    #exibir opções de desconto
    print('{}\nÀ vista dinheiro/cheque: 10% de desconto\nÀ vista no cartão: 5% de desconto\nEm até 2x no cartão: preço formal\n3x ou mais no cartão: 20% de juros\n{}'.format('\033[36m--\033[m' * 20,'\033[36m--\033[m' * 20))
    #opções
    while True:
        quant_parcelamentos = input('\033[mDigite uma das opções\n[1]-À vista\nOu\nDigite o número de parcelamentos\n\033[31m')
        if quant_parcelamentos.isnumeric() == False:
            print('\033[31mOs valores digitados não são numéricos\033[m')
        else:
            quant_parcelamentos = int(quant_parcelamentos)
            if quant_parcelamentos > 10: print('\033[31mNão é possível parcelar em mais de dez vezes\033[m')
            else:
                if quant_parcelamentos > 1:
                    while True:
                        forma_pagamento = input('\033[mDigite uma das opções\n[3]-Cartão\n\033[31m')
                        if forma_pagamento.isnumeric() == False:
                            print('\033[31mOs valores digitados não são numéricos\033[m')
                        else:
                            forma_pagamento = int(forma_pagamento)
                            if forma_pagamento != 3:
                                print('\033[31mTente novamente\033[m')
                                forma_pagamento = input('\033[mDigite uma das opções\n[3]-Cartão\n\033[31m')
                            else:
                                if quant_parcelamentos >= 3 and forma_pagamento == 3:#3x ou mais no cartão: 20% de juros
                                    print('\033[31mO juros para mais de 3x no cartão é de 20%\033[m')
                                    total *= 1.2
                                    valor_Parcela = total/quant_parcelamentos
                                    print(f'O valor será parcelado em \033[35m{quant_parcelamentos:.0f}x\033[m no cartão e cada parcela será de \033[32mR${valor_Parcela:.2f}\033[m')
                                break
                    break
                else: 
                    forma_pagamento = input('\033[mDigite uma das opções\n[1]-Dinheiro\n[2]-Cheque\n[3]-Cartão\n\033[31m')
                    if forma_pagamento.isnumeric() == False:
                        print('\033[31mOs valores digitados não são numéricos\033[m')
                    else:
                        forma_pagamento = int(forma_pagamento)
                        if quant_parcelamentos > 10: print('\033[31mNão é possível parcelar em mais de dez vezes\033[m')
                        #descontos
                        else:
                            if quant_parcelamentos == 1 and forma_pagamento == 1 or quant_parcelamentos == 1 and forma_pagamento == 2:# à vista dinheiro/cheque: 10% de desconto
                                print('\033[32mVocê recebeu um desconto de 10%\033[m')
                                total *= 0.9
                            elif quant_parcelamentos == 1 and forma_pagamento == 3:#à vista no cartão: 5% de desconto
                                print('\033[32mVocê recebeu um desconto de 5%\033[m')
                                total *= 0.95
                            elif quant_parcelamentos == 2 and forma_pagamento == 3:#em até 2x no cartão: preço formal
                                valor_Parcela = total/quant_parcelamentos
                                print(f'O valor será parcelado em \033[35m{quant_parcelamentos:.0f}x\033[m no cartão e cada parcela será de \033[32mR${valor_Parcela:.2f}\033[m')
                        break
    print(f'O valor a ser pago é de \033[33mR${total:.2f}\033[m\n\033[34mObrigada :)\033[m')