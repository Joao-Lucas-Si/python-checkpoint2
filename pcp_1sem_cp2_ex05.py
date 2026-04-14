#Joao Pedro ribeiro Santos 

nome_do_usuario = (input ("digite seu nome aqui: "))
idade_do_usuario = int (input("digite a idade do usuario: "))
renda_mensal = int(input("Qual sua renda mensal:"))
valor_desejavel =  int (input ("qual o  valor que voce deseja retirar: "))
parcelas = int(input("numeros de parcelas desejadas: "))
numeros_permitidos = list(range(3, 25))
p = parcelas
aux = (valor_desejavel * 20)
 
if parcelas not in  numeros_permitidos or idade_do_usuario <= 18 or aux > renda_mensal:
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
    juros_pagos = valor_desejavel - total_pago
 
 
 
print(f"nome:{nome_do_usuario.upper()}")
print(f"idade:{idade_do_usuario}")
print(f"sua renda é de: {renda_mensal}")
print(f"Valor da tentativa: {valor_desejavel}")
print(f"numero de parcelas: {parcelas}")
print(f"valor da parcela:{pmt:.2%}")
print(f"total pago: {total_pago}")
print(f"numero de parcelas: {parcelas}")
print(f"juros pagos: {juros_pagos}")
 
 
