res = []
res.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
soma_respostas = 0
for i in res: 
    soma_respostas += int(i)
if (soma_respostas < 2):
     print("\nInocente")
elif (soma_respostas == 2):
     print("\nSuspeita")
elif (3 <= soma_respostas <= 4):
     print("\nCúmplice")
elif (soma_respostas == 5):
     print("\nAssassino")

