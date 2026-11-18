a = int (input("primeiro número: "))
b = int (input("segundo número: "))
c = int (input("terceiro número: "))

if a >= b and a >= c:
    maior = a

elif b >= c:
    maior = b

else:
    maior = c

print ("o número maior é: ", maior)