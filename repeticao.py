# estrutura de repetição
while True:
    nomeProduto = input("Digite o nome do produto: ")
    precoProduto = int(input("Digite o preço do produto: "))
    continuar = input("Deseja adicionar mais produtos? (s/n) ")
    if continuar.lower() == "n":
        break
    print(f"O produto {nomeProduto} custa {precoProduto} akzs.")
print("Programa encerrado.")
# estrutura de repetição
