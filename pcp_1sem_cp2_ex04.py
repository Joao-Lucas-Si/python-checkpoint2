#Alan 
import os
nome_funcionario = input("Informe o seu nome: ")
print("1 - Gerente")
print("2 - Analista")
print("3 - Assistente")
print("4 - Estagiário")
cargo = int(input("Escolha o seu cargo entre as 4 opções: "))
salario_base=float(input("Informe o seu salario: "))
horas_extras=float(input("Quantas foram as horas extras: "))
faltas_mes=int(input("Quantas vezes você faltou: "))
bonus_recebido=input("Você recebeu um bonus(s/n): ").lower()
def valor_hora_extra(salario_base,horas_extras):
    return (salario_base*0.015)*horas_extras
def desconto_faltas(salario_base,faltas_mes):
    return (salario_base*0.02)*faltas_mes
def calcular_bonus(cargo,bonus_recebido):
    bonus= 0

    if bonus_recebido=="s":
        if cargo== 1:
            bonus= 1000
        elif cargo== 2:
            bonus= 500
        elif cargo== 3:
            bonus= 300
        elif cargo== 4:
            bonus= 100
    else:
        bonus= 0
    return bonus
total_acescimos=valor_hora_extra(salario_base,horas_extras)+ calcular_bonus(cargo,bonus_recebido)
total_descontos= desconto_faltas(salario_base,faltas_mes)
valor_final= salario_base+total_acescimos-total_descontos
os.system("cls" if os.name == 'nt' else 'clear')
print(f"""
------Resultados------
Nome usuario: {nome_funcionario}
salario bruto: {salario_base}
Total de acrescimos(horas extras e bonus): {total_acescimos:.2f}
Total de descontos(faltas): {total_descontos:.2f}
Salario final: {valor_final:.2f} 
""")


