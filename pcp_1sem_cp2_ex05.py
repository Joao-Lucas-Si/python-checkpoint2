#Joao Pedro ribeiro Santos 

nome_do_usuario = (input ("digite seu nome aqui: "))
idade_do_usuario = int (input("digite a idade do usuario: "))
renda_mensal = int(input("Qual sua renda mensal:"))
valor_desejavel =  int (input ("qual o  valor que voce deseja para o emprestimo: "))
parcelas = int(input("numeros de parcelas desejadas(3 a 24 parcelas): "))
numeros_permitidos = list(range(3, 25))
p = parcelas
aux = (renda_mensal * 20)

if parcelas not in  numeros_permitidos or idade_do_usuario <= 18 or valor_desejavel > aux:
    print("voce nao é qualificado ")
    exit()
 
else:
    def calcular_taxa(p):
        if p in range (3 , 7 ):
            return 5 / 100
        elif p in range (7  , 13 ):
            return 8/100
        else :
            return 10 / 100
    taxa = calcular_taxa(parcelas)
   
    pmt = (valor_desejavel * taxa * (1 + taxa)**parcelas) / ((1 + taxa)**parcelas - 1)
 
    total_pago =  pmt * parcelas
    juros_pagos = total_pago - valor_desejavel
valor_da_parcela_sem_juros = valor_desejavel / parcelas
sejuros =  pmt - valor_da_parcela_sem_juros

print("---"*20)
print("---"*20)
print("---"*20)
print(f"nome:{nome_do_usuario.upper()}")
print(f"idade:{idade_do_usuario}")
print(f"sua renda é de: R${renda_mensal}")
print(f"Valor do enprestimo: R${valor_desejavel}")
print(f"numero de parcelas:{parcelas}")
print(f"valor da parcela sem juros: R${valor_da_parcela_sem_juros:.2f}")
print(f"valor do juros por mes: R${sejuros:.2f}")
print(f"valor da parcela com juros: R${pmt:.2f}")
print(f"juros pagos: R${juros_pagos:.2f}")
print(f"total pago: R${total_pago:.2f}")
print("---"*20)
print("---"*20)
print("---"*20)
