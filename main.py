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
		# AUTHENTICATION
		authFile = open("./authentication.txt", "r")
		authFileLines = authFile.readlines()
		isLoggedIn = authFileLines[0].split(" ")[1].startswith("T")

		# CART 
		cartFileReadAndUpdate = open("./cart.txt", "r+")

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

		option = input("Enter specific character to select option >> ")
		if option == "1":
			showProducts()
			return
		elif option == "2":
			showCart()
			return
		elif option == "4":
			if isLoggedIn:
				showLogoutPanel()
				return
		elif option == "0":
			print("See you again!")
			exit()
		else: 
			print("You've entered invalid character.")	
			continue
		
		break


def showProducts():
	while True:
		print("----Products----")
		print("+. Add product")
		print("`. Back")
		print("0. Exit")

		for i in range(len(products)):
			print(f'|{i + 1}\n| {products[i]["name"]} -> {products[i]["price"]}')

		option = input("Enter number to select option >> ")
		if option == "+":
			showAddProductPanel()
			return
		if option == "0":
			print("See you again!")
			exit()
		elif option == "`":
			showLandingPage()
			return
		else:
			print("You've entered invalid character.")


def showAddProductPanel():
	while True:
		print("----Products----")

		print("Enter product number to add it to the cart")
		print("`. Back")
		print("0. Exit")

		for i in range(len(products)):
			print(f'|{i + 1}\n| {products[i]["name"]} -> {products[i]["price"]}')

		option = input("Enter number to select option >> ")
		if option == "`":
			showProducts()
			return
		if option == "0":
			print("See you again!")
			exit()
		if int(option) > 0 and int(option) <= len(products):
			cartFileReadAndUpdate = open("./cart.txt", "r+")
			cartFileLines = cartFileReadAndUpdate.readlines()
			cartFileLines.insert(0, f'{products[int(option) - 1]["name"]}\n')
			cartFileReadAndUpdate.seek(0)
			cartFileReadAndUpdate.writelines(cartFileLines)
			cartFileReadAndUpdate.close()

			print("SUCCESS")
			print("Product added to the cart")
			showLandingPage()
			return
		else: 
			print("You've entered wrong character")

			

def showCart():
	while True:
		cartFileReadAndUpdate = open("./cart.txt", "r+")
		cartFileLines = cartFileReadAndUpdate.readlines()
		cartFileLinesLength = len(cartFileLines)

		print("-----Cart-----")

		if cartFileLinesLength != 0:
			print('-. Remove product')

		print('`. Back')
		print('0. Exit')

		if cartFileLinesLength == 0:
			print("No products found.")
	
		if cartFileLinesLength != 0:
			for i in range(cartFileLinesLength):
				print(f'{i + 1} - {cartFileLines[i].rstrip()}')

		option = input("Enter specific character to select option >> ")
		if option == "0":
			print("See you again!")
			exit()
		elif option == "`":
			showLandingPage()
			return
		elif option == "-" and cartFileLinesLength != 0:
			print("-----Cart-----")

			print("Enter product number to remove it from the cart")
			print('`. Back')
			print("0. Exit")

			for i in range(len(cartFileLines)):
				print(f'{i + 1} - {cartFileLines[i].rstrip()}')

			option = input("Enter specific character to select option >> ")
			if int(option) > 0 and int(option) <= len(cartFileLines):
				cartFileLinesUpdated = cartFileLines[:int(option) - 1] + cartFileLines[int(option):]
				cartFileWrite = open("./cart.txt", "w")
				cartFileWrite.writelines(cartFileLinesUpdated)
				cartFileWrite.close()

				print("SUCCESS")
				print("Product removed")
				continue
			elif option == "`":
				continue
			elif option == "0":
				print("See you again!")
				exit()
			else: 
				print("You've entered invalid character")
				continue
		else:
			print("You've entered invalid character")

def showLogoutPanel():
	print("-----Logout-----")
	print("Are you sure to log out?")

	print("1. Log Out")
	print("2. Cancel")
	print("0. Exit")

	option = input("Enter number to select option >> ")
	if option == "1": 
		authFileWrite = open("authentication.txt", "r+")
		authFileWrite.write("isLoggedIn False")
		authFileWrite.close()

		print("SUCCESS")
		print("You've just logged out")

		showLandingPage()
		return


showLandingPage()



