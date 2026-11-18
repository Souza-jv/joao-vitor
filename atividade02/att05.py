def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
numero = int(input("Calcular o fatorial de: "))
fat = fatorial(numero)

print("Fatorial de numero = ", fat)