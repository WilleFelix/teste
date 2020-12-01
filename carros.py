lista_carros = []
lista_consumo = []

while len(lista_carros) < 5:
    lista_carros.append(input("Digite o nome do carro:"))
    lista_consumo.append(float(input("Digite o consumo do carro(km por litro):")))
    print("novos dados inseridos\n")

resultados = " "
valor_gasolina = 2.25
km = 1000
for j, c in enumerate(lista_carros):
    print("Veículo {}".format(j+1))
    print("Nome: {}".format(c))
    print("Km por litro: {}\n".format(lista_consumo[j]))

    consumo_1 = round(km/lista_consumo[j], 2)
    resultados += "O {} consome {} l e custará R${} quando fizer {} km/h /n".format(c, consumo_1, round(consumo_1*valor_gasolina, 2), km)

print("O carro mais econômico é o {}\n".format(lista_carros[lista_consumo.index(max(lista_consumo))]))
print(resultados)

                               
