nomecandidato = input("Digite o nome do candidato: ")
renda = float(input("Digite a sua renda mensal: "))
idade = int(input("Digite a sua idade: "))
if renda >= 2000 and idade >= 18:
    print(f"Parabens {nomecandidato} seu credito foi aprovado.")
else:
    print(f"Saudações {nomecandidato} , Infelizmente seu credito foi reprovado.")
