USER_FIRST_NAME = str()
USER_LAST_NAME = str()
USER_EMAIL = str()
USER_PASSWORD = str()

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

# ---</MAINPAGE>---
def showLandingPage():
	while True:
		# AUTHENTICATION
		authFile = open("./authentication.txt", "r")
		authFileLines = authFile.readlines()
		isLoggedIn = authFileLines[0].split(" ")[1].startswith("T")

		# CART 
		cartFileReadAndUpdate = open("./cart.txt", "r+")

		productsInCartQuantity = len(cartFileReadAndUpdate.readlines())

		print("\n|================|-------|================|\n|================| Pyzer |================|\n|==============|           |==============|")

		if isLoggedIn: 
			username = authFileLines[1].split(" ")[1].rstrip()
			print(f"Welcome {username}!")
		else:
			print("Welcome!")
		print("Select option.")

		print("1. Products")

		if productsInCartQuantity == 0:
			print("2. Cart")
		else:
			print(f"2. Cart [{productsInCartQuantity}]")

		if productsInCartQuantity > 0:
			print("3. Order")

		if isLoggedIn == False and productsInCartQuantity > 0: 
			print("4. Sign In")
			print("5. Log In")

		if isLoggedIn == False and productsInCartQuantity == 0:
			print("3. Sign In")
			print("4. Log In")

		if isLoggedIn and productsInCartQuantity == 0: 
			print("3. Log Out")
		if isLoggedIn and productsInCartQuantity > 0:
			print("4. Log Out")

		print("0. Exit")


		option = input("Your choice >> ")

		if option == "1":
			showProducts()
			return
		elif option == "2":
			showCart()
			return
		elif option == "3":
			if productsInCartQuantity == 0:
				if isLoggedIn:
					showLogoutPanel()
					return 
				else:
					showSignUpPanel()
					return
			
			showOrderPanel("landingPage")

		elif option == "4":
			if isLoggedIn:
				showLogoutPanel()
				return
			else:
				if productsInCartQuantity == 0:
					showLoginPanel()
					return
				else:
					showSignUpPanel()
					return
		elif option == "5" and isLoggedIn == False:
			showLoginPanel()
			return
		elif option == "0":
			shutdown()
		else: 
			print("\n[!] You've entered invalid character.")	
			continue
		
		break
# ---</MAINPAGE>---


# ---<EXIT>---
def shutdown():
	print("\n----------------------------------------")
	print("See you again!")
	print("----------------------------------------\n")
	exit()
# ---</EXIT>---


# ---<PRODUCTS>---
def showProducts():
	while True:
		print("\n----Products----")
		print("+. Add product")
		print("`. Back")
		print("0. Exit")

		for i in range(len(products)):
			print(f'|<>| {products[i]["name"]} -> {products[i]["price"]}$')

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
			print("\n[!] You've entered invalid character.")

def showAddProductPanel():
	print("\n----Products----")

	print("[1...] Enter product number to add it to the cart")
	print("`. Back")
	print("0. Exit")

	while True:
		for i in range(len(products)):
			print(f'|{i + 1}| {products[i]["name"]} -> {products[i]["price"]}')

		option = input("Your choice >> ")
		if option == "`":
			showProducts()
			return
		if option == "0":
			shutdown()
		if int(option) > 0 and int(option) <= len(products):
			cartFileReadAndUpdate = open("./cart.txt", "r+")
			cartFileLines = cartFileReadAndUpdate.readlines()
			cartFileLines.insert(0, f'{products[int(option) - 1]["name"]}\n')
			cartFileReadAndUpdate.seek(0)
			cartFileReadAndUpdate.writelines(cartFileLines)
			cartFileReadAndUpdate.close()

			print("\n----------------------------------------")
			print("SUCCESS")
			print("Product added to the cart")
			print("----------------------------------------\n")
			showLandingPage()
			return
		else: 
			print("\n[!] You've entered wrong character")

def showRemoveProductPanel():
	while True:
		cartFileReadAndUpdate = open("./cart.txt", "r+")
		cartFileLines = cartFileReadAndUpdate.readlines()
		cartFileLinesLength = len(cartFileLines)

		print("\n-----Cart-----")

		print("Enter product number to remove it from the cart")
		print('`. Back')
		print("0. Exit")

		for i in range(cartFileLinesLength):
			print(f'{i + 1} - {cartFileLines[i].rstrip()}')

		option = input("Enter specific character to select option >> ")
		if int(option) > 0 and int(option) <= cartFileLinesLength:
			cartFileLinesUpdated = cartFileLines[:int(option) - 1] + cartFileLines[int(option):]
			cartFileWrite = open("./cart.txt", "w")
			cartFileWrite.writelines(cartFileLinesUpdated)
			cartFileWrite.close()

			print("\n----------------------------------------")
			print("SUCCESS")
			print("Product removed")
			print("----------------------------------------\n")
			continue
		elif option == "`":
			showCart()
			return
		elif option == "0":
			shutdown()
		else: 
			print("\n[!] You've entered invalid character.")
			continue
# ---<PRODUCTS/>---


# ---<CART>---
def checkTotalAmountOfProductsInCart():
	totalAmount = 0
	cartFileRead = open("./cart.txt", "r")
	cartFileLines = cartFileRead.readlines()
	for line in cartFileLines:
		line = line.rstrip()
		totalAmount += checkProductPrice(line)
	
	return totalAmount

def showCart():
	while True:
		cartFileReadAndUpdate = open("./cart.txt", "r+")
		cartFileLines = cartFileReadAndUpdate.readlines()
		cartFileLinesLength = len(cartFileLines)

		print("\n-----Cart-----")

		if cartFileLinesLength != 0:
			print('1. Order')
			print('-. Remove product')

		print('`. Back')
		print('0. Exit')

		if cartFileLinesLength == 0:
			print("No products found.")
	
		if cartFileLinesLength != 0:
			print("<>---ProductsInCart---<>")
			for i in range(cartFileLinesLength):
				print(f'<> {cartFileLines[i].rstrip()}')
			print(f"<>---TotalAmount >> {checkTotalAmountOfProductsInCart()}$")

		option = input("Your choice >> ")
		if option == "0":
			shutdown()
		elif option == "`":
			showLandingPage()
			return
		elif option == "1" and cartFileLinesLength != 0:
			showOrderPanel("cart")
			return
		elif option == "-" and cartFileLinesLength != 0:
			showRemoveProductPanel()
			return
		else:
			print("\n[!] You've entered invalid character.")

def checkProductPrice(productName):
	for product in products:
		if product["name"] == productName:
			return product["price"]
# ---</CART>---


# ---<ORDER>---
def showOrderPanel(redirectedFrom):
	while True:
		print("\n-----Order-----")
		print(f"Total Amount: {checkTotalAmountOfProductsInCart()}$")
		print("Are you sure to order?")

		print("1. Order")
		print("2. Cancel")
		print("`. Back")
		print("0. Exit")

		option = input("Your choice >> ")
		if option == "1":
			# CLEAN CART
			cartFileWrite = open("./cart.txt", "w")
			cartFileWrite.writelines("")
			cartFileWrite.close()

			print("\n------------------------------")
			print("Thank you very much for shopping in our shop.\nYour clothes will be delivered in up to 3 days.")
			print("------------------------------\n")
			showLandingPage()
			return
		elif option == "2" or "`":
			if redirectedFrom == "cart":
				showCart()
				return
			if redirectedFrom == "landingPage":
				showLandingPage()
				return
		elif option == "0":
			shutdown()
		else:
			print("\n----------------------------------------")
			print("You've entered invalid character.")
			print("----------------------------------------\n")
# ---</ORDER>---


# ---<AUTHENTICATION>---
def showSignUpPanel():
	
	usersFileReadAndUpdate = open("./users.txt", "r+")
	usersFileLines = usersFileReadAndUpdate.readlines()

	firstName = str()
	lastName = str()
	email = str()
	password = str()

	print("\n-----SignUp-----")
	print("`. Back")
	print("0. Exit")

	for i in range(4):
		while True:
			if i == 0:
				firstName = input("Enter first name >> ")

				if firstName == "`":
					showLandingPage()
					return	
				if firstName == "0":
					shutdown()

				break
			elif i == 1:
				lastName = input("Enter last name >> ")

				if lastName == "`":
					showLandingPage()
					return	
				if lastName == "0":
					shutdown()

				break
			elif i == 2:
				email = input("Enter email >> ")

				if email == "`":
					showLandingPage()
					return
				if email.count("@") == 0 or email.count(".") == 0:
					print("\n[!] Invalid email format. Try again.")
					continue	
				if email == "0":
					shutdown()
				
				# check if email is not busy
				isEmailBusy = False
				for j in range(len(usersFileLines)):
					if usersFileLines[j].startswith("user"):
						if usersFileLines[j + 3].split(" ")[1].rstrip() == email:
							print("\n[!] This email is busy. Type another email.")
							isEmailBusy = True
							break

				if isEmailBusy:
					continue
				else:
					break
			else:
				password = input("Enter password >> ")

				if password == "`":
					showLandingPage()
					return
				if password == "0":
					shutdown()
				if len(password) < 5:
					print("\n[!] Password has to be at least 7 characters long.")
					continue	
				
				break

	# check how many users are signed
	userCount = int()
	if len(usersFileLines) == 0:
		userCount = 0
	else:
		userCount = int(usersFileLines[0].rstrip()[5:len(usersFileLines[0]) - 2]) + 1

	usersFileLines.insert(0, "----------------------------------------\n")
	usersFileLines.insert(0, f"--password {password} \n")
	usersFileLines.insert(0, f"--email {email}\n")
	usersFileLines.insert(0, f"--lastName {lastName}\n")
	usersFileLines.insert(0, f"--firstName {firstName}\n")
	usersFileLines.insert(0, f"user[{userCount}]\n")

	usersFileReadAndUpdate.seek(0)
	usersFileReadAndUpdate.writelines(usersFileLines)
	usersFileReadAndUpdate.close()

	print("\n----------------------------------------")
	print("SUCCES")
	print("You've signed up. Now it's time to log in.")
	print("----------------------------------------\n")
	showLoginPanel()

def showLoginPanel():
	email = str()
	password = str()
	correctPassword = str()
	userLineIndexInUsersFile = int()

	print("\n-----Login-----")
	print("`. Back")
	print("0. Exit")

	for i in range(2):
		while True:
			if i == 0:
				email = input("Enter email >> ")

				if email == "`": 
					showLandingPage()
					return
				if email == "0":
					shutdown()
				
				# finding email in database (in users.txt)
				emailFound = False

				usersFileRead = open("./users.txt", "r")
				usersFileLines = usersFileRead.readlines()
				for j in range(len(usersFileLines)):
					if usersFileLines[j].startswith("--email"):
						if usersFileLines[j].rstrip().split(" ")[1] == email:
							correctPassword = usersFileLines[j + 1].rstrip().split(" ")[1]
							
							emailFound = True
							userLineIndexInUsersFile = j - 3

				usersFileRead.close()

				if emailFound: 
					break
				else:
					print("\n[!] This email seems to not exist in our database. Try again.")
					continue
			
			else:
				while True:
					password = input("Enter password >> ")

					if password == "`":
						showLandingPage()
						return
					if password == "0":
						shutdown()

					if password != correctPassword:
						print("\n[!] Password is incorrect. Try again.")
						continue
					else:
						break

			# SAVE DATA ABOUT USER AFTER USER LOG IN
			usersFileRead = open("users.txt", "r")
			usersFileLines = usersFileRead.readlines()

			USER_FIRST_NAME = usersFileLines[userLineIndexInUsersFile + 1].rstrip().split(" ")[1]
			USER_LAST_NAME = usersFileLines[userLineIndexInUsersFile + 2].rstrip().split(" ")[1]
			USER_EMAIL = usersFileLines[userLineIndexInUsersFile + 3].rstrip().split(" ")[1]
			USER_PASSWORD = usersFileLines[userLineIndexInUsersFile + 4].rstrip().split(" ")[1]

			# CHANGE STATUS IN AUTH FILE
			authFileWrite = open("./authentication.txt", "w")
			authFileWrite.write(f"isLoggedIn True\n--firstName {USER_FIRST_NAME}\n--lastName {USER_LAST_NAME}\n--email {USER_EMAIL}\n--password {USER_PASSWORD}\n")
			authFileWrite.close()

			print("\n----------------------------------------")
			print("SUCCESS")
			print("You've just logged in.")
			print("----------------------------------------\n")
			showLandingPage()
			return

def showLogoutPanel():
	while True:
		print("\n-----Logout-----")
		print("Are you sure to log out?")

		print("1. Log Out")
		print("2. Cancel")
		print("`. Back")
		print("0. Exit")

		option = input("Your choice >> ")
		if option == "1": 
			authFileWrite = open("authentication.txt", "r+")
			authFileWrite.write("isLoggedIn False")
			authFileWrite.close()

			print("\n----------------------------------------")
			print("SUCCESS")
			print("You've just logged out")
			print("----------------------------------------\n")

			showLandingPage()
			return
		elif option == "2" or "`":
			showLandingPage()
			return
		else: 
			print("\n[!] You've entered invalid character")
# ---</AUTHENTICATION>---


showLandingPage()



