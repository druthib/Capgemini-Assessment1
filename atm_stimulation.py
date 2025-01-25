def checkBalance(totalbalance):
    pin=int(input("enter the pin"))
    balance=totalbalance if pin==123 else'invalid Pin'
    print(f'Balance is:{balance}')
    
def depositMoney(totalbalance):
    depositeMoney=int(input("enter the money to be depossited"))
    pin=int(input("enter the pin"))
    if pin==123: 
        totalbalance=depositeMoney+totalbalance
        print(f'total balance after depositing {depositeMoney} money is:{totalbalance}')
    else :
        print('invalid pin')
    return totalbalance
    
def withdrawMoney(totalbalance):
    withdrawAmount=int(input("enter the amount to be withdrawn"))
    if(withdrawAmount>totalbalance or withdrawAmount==0):
        print('insufficient balance. Cant be Withdrwan.')
    else:
        pin=int(input("enter the pin"))
        if pin==123:
            print(f'{withdrawAmount} has been withdrwan')
            totalbalance=(totalbalance)-withdrawAmount
            print(f'remaining total balance is{totalbalance}')
        else :
            print('invalid pin')
    return totalbalance

def exit():
    print('thank you')
    return 1

totalbalance= 1000  
while True:
    print('1.Check Balance \n2.Deposit Money \n3.Withdraw Money \n4.Exit')
    choice = int(input("Enter your Choice:"))
    if choice==1:
        checkBalance(totalbalance)
    elif choice==2:
        depositMoney(totalbalance)
    elif choice==3:
        withdrawMoney(totalbalance)
    elif choice==4:
        exit()
        break
    else:
        print('invalid choice')
    continue_choice = input("Do you want to continue? (yes/no): ").lower()
    if continue_choice != 'yes':
        print('Exiting the program.')
        break
