numero_secreto = 7
tentativas = 1
palpite = int(input("escolha um numero de 1 a 10: "))

while palpite != numero_secreto:
     if palpite < numero_secreto:
             print ("é maior ")
     elif palpite > numero_secreto:
            print("é menor ")

     palpite = int(input("Não foi dessa vez,tente novamente"))
     tentativas += 1

print("acertou em",tentativas, "tentativas")




