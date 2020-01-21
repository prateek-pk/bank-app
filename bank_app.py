
choice=0
cid=123456789
cb=1000
cp='qwertyuiop'
ministatement=[]

#menu
def menu():
    global choice
    print('''----Welcome to AAPNA BANK----

    --MENU--
    1. Check Balance
    2. Mini Statement
    3. Withdraw cash
    4. Deposit cash
    5. Exit''')
    choice=int(input('--please enter your choice--'))



def ac_bal():
    print('your account balance is', cb)
    

def min_stat():
    for i in ministatement:
        if(i>0):
            print(f"{i} is credit to your account")
        else:
            print(f"{-i} is debited from your balance")
    

def withdraw():
    global cb
    w=int(input('Enter the amount you want to withdraw  '))
    if (w<=cb and w>0):
        ministatement.insert(0,-w)
        print(w,' from your account has been deducted')
        cb-=w
        
    else:
        print('Insufficient Balance:Enter less amount')
        withdraw()



def deposit():
    global cb
    d=int(input("Enter the amount you want to deposit:"))
    ministatement.insert(0,+d)
    print(d, ' has been deposited in your account')
    cb+=d
    
while(True):
    menu()
    #running fuctions
    if(choice==1):
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
