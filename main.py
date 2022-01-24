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
			username = authFileLines[1].split(" ")[1].rstrip()
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
			else:
				showSignUpPanel()
				return
		elif option == "5" and isLoggedIn == False:
			showLoginPanel()
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


def showSignUpPanel():
	usersFileReadAndUpdate = open("./users.txt", "r+")
	usersFileLines = usersFileReadAndUpdate.readlines()

	firstName = str()
	lastName = str()
	email = str()
	password = str()

	for i in range(4):
		while True:
			print("-----SignUp-----")
			print("`. Back")
			print("0. Exit")

			if i == 0:
				firstName = input("Enter first name >> ")

				if firstName == "`":
					showLandingPage()
					return	
				if firstName == "0":
					print("See you again!")
					exit()

				break
			elif i == 1:
				lastName = input("Enter last name >> ")

				if lastName == "`":
					showLandingPage()
					return	
				if lastName == "0":
					print("See you again!")
					exit()

				break
			elif i == 2:
				email = input("Enter email >> ")

				if email == "`":
					showLandingPage()
					return
				if email.count("@") == 0 or email.count(".") == 0:
					print("Invalid email format. Try again.")
					continue	
				if email == "0":
					print("See you again!")
					exit()
				
				# check if email is not busy
				isEmailBusy = False
				for j in range(len(usersFileLines)):
					if usersFileLines[j].startswith("user"):
						if usersFileLines[j + 3].split(" ")[1].rstrip() == email:
							print("This email is busy. Type another email.")
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
					print("See you again!")
					exit()
				if len(password) < 5:
					print("Password has to be at least 7 characters long.")
					continue	
				
				break

	# check how many users are signed
	userCount = int(usersFileLines[0].rstrip()[5:len(usersFileLines[0]) - 2]) + 1
	print(userCount)

	usersFileLines.insert(0, "----------------------------------------\n")
	usersFileLines.insert(0, f"--password {password} \n")
	usersFileLines.insert(0, f"--email {email}\n")
	usersFileLines.insert(0, f"--lastName {lastName}\n")
	usersFileLines.insert(0, f"--firstName {firstName}\n")
	usersFileLines.insert(0, f"user[{userCount}]\n")

	usersFileReadAndUpdate.seek(0)
	usersFileReadAndUpdate.writelines(usersFileLines)
	usersFileReadAndUpdate.close()

	print("SUCCES")
	print("You've signed up. Now it's time to log in.")
	showLoginPanel()


def showLoginPanel():
	email = str()
	password = str()
	correctPassword = str()
	userLineIndexInUsersFile = int()

	print("-----Login-----")
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
					print("See you again!")
					exit()
				
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
					print("This email seems to not exist in our database. Try again.")
					continue
			
			else:
				while True:
					password = input("Enter password >> ")

					if password == "`":
						showLandingPage()
						return
					if password == "0":
						print("See you again!")
						exit()

					if password != correctPassword:
						print("Password is incorrect. Try again.")
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

			print("SUCCESS")
			print("You've just logged in.")
			showLandingPage()
			return
				

def showLogoutPanel():
	while True:
		print("-----Logout-----")
		print("Are you sure to log out?")

		print("1. Log Out")
		print("2. Cancel")
		print("`. Back")
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
		elif option == "2" or "`":
			showLandingPage()
			return
		else: 
			print("You've entered invalid character")


showLandingPage()



