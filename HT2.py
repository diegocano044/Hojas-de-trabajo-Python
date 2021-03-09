#Ej. 1
print("Triangulo")
nume = int(input("Por favor ingrese un numero entero positivo \n"))
for i in range(nume):
    for j in range(i+1):
        print(end="")
    print("")


#Ej. 2
numero = int(input("Por favor ingrese un número positivo: \n"))
for i in range(numero, -1, -1):
    print(i, end=", ")


#Ej. 3
num = input("Por favor ingrese un numero: \n")
numero = int(num)
contador = 0
verificar= False
for i in range(1,numero+1):
    if (numero% i)==0:
       contador = contador + 1
    if contador >= 3:
        verificar=True
        break
if contador==2 or verificar==False:
    print ("El numero es primo")
else: print ("El numero no es primo")