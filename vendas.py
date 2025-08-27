produto = 'Computador'
preco = 201.99
quantidade = int(input('Quantas unidades você quer comprar? '))
resultado = preco * quantidade
nomeCliente = input('Qual o seu nome? ')
doctoCliente = input('Qual o seu documento? ')  
print(f'O cliente {nomeCliente} com o documento {doctoCliente} comprou {quantidade} unidades do produto {produto} cada um custa {preco} akzs. O total da compra é {resultado:.2f} akzs')
print(f'O total da compra é: {resultado:.2f} akzs')  # Formatação para 2 casas decimais