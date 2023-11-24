# [LP-PY-A02]Escreva um código em Python que peça três números e determine:
# - O maior número
# - O menor número
# - Se algum deles é igual e se for qual é o número igual

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = max(num1,num2,num3)
menor = min(num1,num2,num3)

print("-"*30)
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print("-"*30)

if (num1 == num2) and (num1 == num3):
    print(f"Todos os números são iguais")
elif (num1 == num2):
    print(f"O número 1 '{num1}' é igual ao número 2 '{num2}'")
elif (num1 == num3):
    print(f"O número 1 '{num1}' é igual ao número 3 '{num3}'")
elif (num2 == num3):
    print(f"O número 2 '{num2}' é igual ao número 3 '{num3}'")
else:
    print(f"INFO:\nNão há números repetidos")