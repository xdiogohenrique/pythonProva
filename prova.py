num1 = int(input("Insira o primeiro valor:"))
num2 = int(input("Insira o segundo valor:"))
num3 = int(input("Insira o terceiro valor:"))

if num1 > 0 and num1 > num2:
    print("num1 positivo e maior que num2")
elif num2 < 0 and num2 > num3: 
    print("Num2 negativo e maior que num3")
else:
    print("Num3 é negativo")