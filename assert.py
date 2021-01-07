def buy(sum, wallet):
	try:
		assert wallet >= sum
		wallet -= sum
		return wallet
	except AssertionError:
		print('Недостаточно средств!')
		return wallet

wallet = 150
wallet = buy(155, wallet)
print(wallet)
