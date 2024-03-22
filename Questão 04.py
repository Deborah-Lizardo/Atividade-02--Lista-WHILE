cont = 0
soma = 0
quantnum = int(input("quantos numeros voce quer digitar? "))

while cont < quantnum:
    num = int(input("digite um numero maior que dez: "))

    if num >= 10:
        soma += num
        cont += 1
    else:
        print(f"digite outro numero")

print(soma)