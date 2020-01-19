#bank application


#variables
choice=0
cid=123456789
cb=1000
cp='qwertyuiop'
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
		withdraw()
	elif (choice==4):
		deposit()
	elif (choice==5):
		exit()
	else:
		print('NETWORK ERROR!! : PLEASE RETRY')
		menu()

def ac_bal():
	print('your account balance is', cb)
	menu()

def min_stat():
	for i in ministatement:
		print(i)
	menu()

def withdraw():
	global cb
	w=int(input('Enter the amount you want to withdraw  '))
	if (w<=cb):
		ministatement.pop()
		ministatement.insert(0,w)
		print(w,' from your account has been deducted')
		cb-=w
		menu()
	else:
		print('Insufficient Balance:Enter less amount')
		withdraw()



def deposit():
	global cb
	d=int(input("Enter the amount you want to deposit:"))

	ministatement.pop()
	ministatement.insert(0,d)
	print(d, ' has been deposited in your account')
	cb+=d
	menu()


menu()
