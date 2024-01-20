# 3. Crie um dicionário representando um carrinho de compras.
# Adicione produtos (chaves) e quantidades (valores) ao carrinho.
# Calcule o total do carrinho de compra.

carrinhoDeCompras = {}
product_names = []
product_quantity = []
qntd = int(input('Quantos produtos? \n'))
index = 0

for item in range(qntd):
    key = input(f'Nome do {item + 1}º produto: \n')
    value = float(input('Quantidade: \n'))
    
    product_names.append(key)
    product_quantity.append(value)
    
for key_name, value_quantity in zip(product_names, product_quantity):
    carrinhoDeCompras[key_name] = value_quantity

totalSum = sum(carrinhoDeCompras.values())
print(f'Total do seu carrinho de compras: {totalSum}')

    


