# João Evangelista

entrada = input("Digite seus valores aqui: ")
valores = list(map(float, entrada.split()))
 
valores_ordenados = sorted(valores, reverse=True)
A, B, C = valores_ordenados
#print(f"A={A} B={B} C={C}")
 
# teste = A>=B+C
# print(teste)
 
 
 
if A>=B+C:
    print("não forma triangulo")
 
else:
    x = A**2
    y = B**2+C**2
 
    if x == y:
        print("triangulo retangulo")
    elif x > y:
        print("triangulo obtusangulo")
    else :
        print("triangulo acutangulo")
     
 
    #VERIFICACAO POR LADOS
    if A==B==C:
        print("triangulo equilatero")
    elif A==B or A==C or B==C:
        print("triangulo isosceles")