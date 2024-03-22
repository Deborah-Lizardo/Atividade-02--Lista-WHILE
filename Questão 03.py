numeros_pares = 0
numeros_impares = 0
soma_pares = 0
soma_impares = 0

while numeros_pares < 5 and soma_impares <= 30:
    numero = int(input("Digite um número inteiro positivo: "))
    
    if numero < 0:
        print("Por favor, digite um número positivo.")
        continue
    
    if numero % 2 == 0:
        print("O número é par.")
        numeros_pares += 1
        soma_pares += numero
    else:
        print("O número é ímpar.")
        numeros_impares += 1
        soma_impares += numero
    
    if numeros_pares >= 5:
        break

print("\nTotal de números pares digitados:", numeros_pares)
print("Total de números ímpares digitados:", numeros_impares)
print("Soma dos números pares digitados:", soma_pares)
print("Soma dos números ímpares digitados:", soma_impares)