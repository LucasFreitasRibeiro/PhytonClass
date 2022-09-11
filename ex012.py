precoproduto = float(input("Qual o preco do produto: R$"))
desconto = float(input("Qual o desconto: "))
novopreco = precoproduto - (precoproduto * desconto / 100)
print(f"O produto que custava R${precoproduto:.2f}, com o desconto de {desconto:.2f}% vai custar R${novopreco:.2f}")




