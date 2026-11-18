senha_correta = "12345"
tentativas = 0
max_tentativas = 3
acertou = False
while tentativas < max_tentativas and not acertou:
    senha = input("Senha: ")
    
    if senha == senha_correta:
        acertou = True
    else:
        print("Senha errada.")
        tentativas += 1
    if acertou:
         print("Acesso liberado!")
    else:
         print("Acesso bloqueado.")