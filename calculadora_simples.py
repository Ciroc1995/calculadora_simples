# *********************** Como construir uma calculadora simples ***********************
# 1. Adição
# 2. Subtração
# 3. Divisão
# 4. Multiplicação

print("Selecione a operação que deseja realizar: ")
print("1. Adição")
print("2. Subtração")
print("3. Divisão")
print("4. Multiplicação")

operacao = int(input("Escolha a operação: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

adicao = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

if(operacao == 1):
    print(adicao)
elif(operacao == 2):
    print(subtracao)
elif (operacao == 3):
    print(divisao)
elif(operacao == 4):
    print(multiplicacao)
else:
    print("Entrada inválida")
