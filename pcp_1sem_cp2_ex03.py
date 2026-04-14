# Enzo
cp1 =  float(input("qual sua nota na cp1: "))
cp2 = float(input("qual sua nota na cp2: "))
cp3 = float(input("qual sua nota na cp3: "))
sp1 = float(input("qual sua nota na sp1: "))
sp2 = float(input("qual sua nota na sp2: "))
gs = float(input("qual sua nota na gs: "))

# João Lucas

def min(notas):
    menor = None

    for nota in notas:
        if menor == None:
            menor = nota
        elif menor > nota:
            menor = nota

    return menor



def nota_checkpoint(cp1, cp2, cp3):
    return cp1 + cp2 + cp3 - min([cp1, cp2, cp3])


# Enzo

def nota_sprint(cp1, cp2, cp3, sprint1, sprint2):
    return (nota_checkpoint(cp1, cp2, cp3) + sprint1 + sprint2) / 4


def nota_bruta(cp1, cp2, cp3, sp1, sp2, gs):
    return nota_sprint(cp1, cp2, cp3, sp1, sp2) * 0.4 + gs * 0.6

nota_total = nota_bruta(cp1, cp2, cp3, sp1, sp2, gs)

# João Lucas

nota = nota_total * 0.4


print(f"""
media do primeiro semestre: {nota}
""")

