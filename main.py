if __name__ == '__main__':
	while True:
		print('Menu')
		print('-------------')
		print('1. Encode\n2. Decode\n3. Quit')

		user_input = int(input('Please enter an option: '))

		# Decode function 
		if user_input == 1:
			original_password = str(input('Please enter your password to encode: '))
			password_list = list(original_password)
			new_list = []
			for i in password_list:
				if int(i) not in range(7):
					i = int(i) + 3
					i = str(i)[1]
					new_list.append(str(i))
				else:
					i = int(i) + 3
					new_list.append((str(i)))




					
