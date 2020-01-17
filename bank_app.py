#bank application

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
	break
else:
	print('NETWORK ERROR!! : PLEASE RETRY')
	menu()


cid=0
cb=0.0
cp=0
ministatement=[1,2,3,4,5]

def ac_bal():
	print(cb)

def min_stat():
	for i in ministatement:
		print(i)

def withdraw():
	
	while (true):
		w=int(input('Enter the amount you want to withdraw'))
	
		if (w<=cb):
		ministatement.pop()
		ministatement.insert(w)
		cb-=w
		break
	
	else:
		print('tum gareeb ho')


def deposit():
	d=int(input("Enter the amount you want to deposit:"))

	ministatement.pop()
	ministatement.insert(d)
	cb+=d
