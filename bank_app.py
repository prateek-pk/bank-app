cid=0
cb=0.0
cp=0
ministatement=[cb for i in range(0,count)]
count=0

def ac_bal():
	print(cb)

def min_stat():
	for i in ministatement:
		print(f"your  transaction:{i}")

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
	count++


def deposit():
	d=int(input("enter the amount you want to deposit:"))

	ministatement.pop()
	ministatement.insert(d)
	cb+=d
	count++
