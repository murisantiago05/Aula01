'''
def mult(primeiro, segundo):
    return primeiro * segundo

primeiro = int(input("Digite um numero: "))
segundo = int(input("Digite outro numero: "))


#resultado = 

print(mult(primeiro, segundo))

'''
'''def calcular_media(valores):
    return sum(valores) / len(valores)

resultado = [7,5,3,8]

print(calcular_media(resultado))'''

def calcular_media(notas):
    return sum(notas) / len(notas)

notas = [] 
for i in range(4):
nota = float(input(f"digite sua nota {i+1}: "))
notas.append(nota)

resultado = calcular_media(notas)
print("sua média é", resultado)

'''n1 = float(input("Digite sua Nota1: "))
n2 = float(input("Digite sua Nota2: "))
n3 = float(input("Digite sua Nota3: "))
n4 = float(input("Digite sua Nota4: "))

resultado = [n1,n2,n3,n4]

print(calcular_media(resultado))'''

