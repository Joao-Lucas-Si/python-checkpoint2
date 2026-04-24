
#joao Pedro Ribeiro Santos 

def pode_aprovar(idade, renda, valor):
    aux = renda * 20
    if idade <= 18 or valor > aux:
        return False
    return True

def definir_taxa(parcelas):
    if parcelas in range(3, 7):
        return 5 / 100
    elif parcelas in range(7, 13):
        return 8 / 100
    else:
        return 10 / 100

def calcular_parcela(valor, taxa, parcelas):
   
    return (valor * taxa * (1 + taxa)**parcelas) / ((1 + taxa)**parcelas - 1)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

nome_do_usuario = input("Digite seu nome aqui: ")
idade_do_usuario = int(input("Digite a idade do usuario: "))
renda_mensal = float(input("Qual sua renda mensal: "))
valor_desejavel = float(input("Qual o valor que voce deseja para o emprestimo: "))
parcelas = int(input("Numeros de parcelas desejadas (3 a 24 parcelas): "))

numeros_permitidos = list(range(3, 25))


if parcelas not in numeros_permitidos or not pode_aprovar(idade_do_usuario, renda_mensal, valor_desejavel):
    print("Você não é qualificado para este empréstimo.")
    exit()
else:
   
    taxa = definir_taxa(parcelas)
    pmt = calcular_parcela(valor_desejavel, taxa, parcelas)
    total_pago = calcular_total(pmt, parcelas)
    juros_pagos = calcular_juros(total_pago, valor_desejavel)
    
    valor_da_parcela_sem_juros = valor_desejavel / parcelas
    sejuros = pmt - valor_da_parcela_sem_juros

    print("---"*20)
    print("---"*20)
    print("---"*20)
    print(f"Nome: {nome_do_usuario.upper()}")
    print(f"Idade: {idade_do_usuario}")
    print(f"Sua renda é de: R${renda_mensal:.2f}")
    print(f"Valor do empréstimo: R${valor_desejavel:.2f}")
    print(f"Número de parcelas: {parcelas}")
    print(f"Valor da parcela sem juros: R${valor_da_parcela_sem_juros:.2f}")
    print(f"Valor dos juros por mês: R${sejuros:.2f}")
    print(f"Valor da parcela com juros: R${pmt:.2f}")
    print(f"Juros pagos: R${juros_pagos:.2f}")
    print(f"Total pago: R${total_pago:.2f}")
    print("---"*20)
    print("---"*20)
    print("---"*20)