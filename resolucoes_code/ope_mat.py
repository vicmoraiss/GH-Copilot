# Solicitar como entrada dois números inteiros e realizar uma operação simples entre eles.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else:
    print("Operação inválida. Tente novamente.")
