products = []
while True:
	name = input('請輸入購買的商品:')
	if name == 'q':
		break
	price = input('請輸入價格:')
	products.append([name, price])
print(products)

