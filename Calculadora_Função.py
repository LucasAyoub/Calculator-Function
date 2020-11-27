num = float(input("Digite o primeiro número: "))
num1 = float(input("Digite o segundo número: "))

print("Escolha a operação desejada: ")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
operacao = int(input("Escolha: "))

def somar(num, num1):
    return num + num1



def subtrair(num, num1):
    return num - num1



def multiplicar(num, num1):
    return num * num1



def divisao(num, num1):
    return num / num1



def realizarOperacao(op, num, num1):
    if op == 1:
        print("A soma entre {} + {} = {}".format(num, num1, somar(num, num1)))
    elif op == 2:
        print("A subtração entre {} - {} = {}".format(num, num1, subtrair(num, num1)))
    elif op == 3:
        print("A multiplicação entre {} * {} = {}".format(num, num1, multiplicar(num, num1)))
    elif op == 4:
        print("A divisão entre {} / {} = {}".format(num, num1, divisao(num, num1)))
    else:
        print("Comando não encontrado")
        return 0
realizarOperacao(operacao, num, num1)