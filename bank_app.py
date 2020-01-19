#bank application


#variables
choice=0
cid=123456789
cb=1000
cp='qwertyuiop'
tb=cb
ministatement=[1,2,3,4,5]

#menu
def menu():
	print('''----Welcome to AAPNA BANK----
		--MENU--
		1. Check Balance
		2. Mini Statement
		3. Withdraw cash
		4. Deposit cash
		5. Exit''')
	choice=int(input('--please enter your choice--'))
	#running fuctions
	if (choice==1):
		ac_bal()
	elif (choice==2):
		min_stat()
	elif (choice==3):
		withdraw(cb)
	elif (choice==4):
		deposit(cb)
	elif (choice==5):
		exit()
	else:
		print('NETWORK ERROR!! : PLEASE RETRY')
		menu()

def ac_bal():
	print(cb)
	menu()

def min_stat():
	for i in ministatement:
		print(i)
	menu()

def withdraw(cb):
	w=int(input('Enter the amount you want to withdraw'))
	if (w<=tb):
		ministatement.pop()
		ministatement.insert(w,1)
		print(w,'from your account has been deducted')
		cb=tb-w
		menu()
	else:
		print('Insufficient Balance:Enter less amount')
		withdraw()



def deposit(cb):
	d=int(input("Enter the amount you want to deposit:"))

	ministatement.pop()
	ministatement.insert(d,1)
	print(d, 'has been deposited in your account')
	cb=tb+d
	menu()


menu()
