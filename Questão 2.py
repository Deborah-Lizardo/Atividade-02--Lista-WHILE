soma=0
contador=0
while contador<10:
    nota=float(input("DIGITE UMA NOTA: "))
    soma+=nota
    contador+=1
media=soma/contador
print(f"Sua média é: {media:.2f}")