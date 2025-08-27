nomeComprador = 'Theo Augusto'
produto = 'Celular'
precoCell = 1507.27
quantidade = 3  

print('O cliente: ', nomeComprador)
print('Comprou: ', quantidade)
print('unidades do produto: ', produto)    
print('Cada um custa: ', precoCell, 'akzs')
total = precoCell * quantidade
print('O total da compra é: ', total, 'akzs')
print(f'O cliente {nomeComprador} comprou {quantidade} unidades do produto {produto} cada um custa {precoCell} akzs. O total da compra é {total:.2f} akzs')
print(f'O total da compra é: {total:.2f} akzs')  # Formatação para 2 casas decimais