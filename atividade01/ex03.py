idade = int(input("digite a sua idade: "))
if idade < 16:
    print("ainda não vota! ")
elif idade == 16 or idade == 17 or idade >= 70:
    print("voto opcional.")
else:
    print("voto obrigatório")

