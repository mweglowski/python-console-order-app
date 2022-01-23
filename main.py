# AUTHENTICATION
authFile = open("./authentication.txt", "r")
authFileLines = authFile.readlines()
isLoggedIn = authFileLines[0].split(" ")[1].startswith("T")

# CART
cartFileReadAndUpdate = open("./cart.txt", "r+")
cartFileLines = cartFileReadAndUpdate.readlines()

products = [
	{
		"id": 0,
		"name": "hoodie",
		"price": 50,
	},
	{
		"id": 1,
		"name": "tshirt",
		"price": 25,
	},
	{
		"id": 2,
		"name": "cap",
		"price": 20,
	},
	{
		"id": 3,
		"name": "sneakers",
		"price": 100,
	},
	{
		"id": 4,
		"name": "socks",
		"price": 5,
	},
]

def showLandingPage():
	while True:
		productsInCartQuantity = len(cartFileReadAndUpdate.readlines())

		print("|================|-------|================|\n|================| Pyzer |================|\n|==============|           |==============|")
		if isLoggedIn: 
			username = authFileLines[1].split(" ")[1]
			print(f"Welcome again {username}!")
		else:
			print("Welcome!")
		print("Select option.")

		print("1. Products")
		if productsInCartQuantity == 0:
			print("2. Cart")
		else:
			print(f"2. Cart [{productsInCartQuantity}]")
		print("3. Previous orders")
		if isLoggedIn == False: 
			print("4. Sign In")
			print("5. Log In")
		if isLoggedIn: 
			print("4. Log Out")
		print("0. Exit")

		option = input("Enter number to select option >> ")
		if option == "1":
			showProducts()
		elif option == "4":
			if isLoggedIn:
				print("We need to update auth file!")
		else: 
			print("You've entered invalid character.")	
			continue
		
		break


def showProducts():
	print("----Products----")
	print("`. Back")
	print("Type num of product to add it to the cart.")
	print("0. Exit")

	for i in range(len(products)):
		print(f'|{i + 1}\n| {products[i]["name"]} -> {products[i]["price"]}')

	option = input("Enter number to select option >> ")
	if option == "0":
		print("See you again!")
		exit()
	elif option == "`":
		showLandingPage()
	elif option > len(products):
		print("You've entered invalid character.")
	else:
		cartFileLines.insert(0, f'{products[int(option) - 1]["name"]}\n')
		cartFileReadAndUpdate.seek(0)
		cartFileReadAndUpdate.writelines(cartFileLines)



showLandingPage()



