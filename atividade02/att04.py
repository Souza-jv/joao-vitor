N = int(input("Mostrar os pares de 1 até: "))
contador = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)
        contador += 1
print("São contados números pares.")