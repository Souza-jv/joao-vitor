n1 = float (input("primeiro número: "))
n2 = float (input("segundo número: "))
print("MENU")
print("1 - somar")
print("2 - dividir")
print("3 - subtrair")
print("4 - multiplicar")

operacao = int (input("operacao: "))
if operacao == 1:
    resultado = n1 + n2
    print("Resultado: ", resultado)
elif operacao == 2:
    resultado = n1 - n2
    print("Resultado: ", resultado)
elif operacao == 3:
    resultado = n1 * n2
    print("Resultado: ", resultado)
elif operacao == 4:
    if n2 == 0:
        print("Não dá para dividir por zero.")
    else:
        resultado = n1 / n2
        print("Resultado: ", resultado)
else:
    print("Operação inválida.")
