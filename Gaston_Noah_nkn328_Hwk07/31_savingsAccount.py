def savingsAccount():
    '''
Creates a menu for checking, withdrawing from, and depositing into a bank account
@param bal=balance of account
@param x=amount withdrawn or deposited
    '''
    try:
        print("Options:")
        bal=1000
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. Obtain balance")
        print("4. Quit\n")
        while True:
            num = int(input("Make a selection from the menu: "))
            if num == 1:
                x=float(input("Enter amount to deposit: "))
                bal=bal+x
            elif num == 2:
                x=float(input("Enter amount of withdrawal: "))
                bal = bal - x
            elif num == 3:
                print("The balance is $", bal, sep="")
            elif num == 4:
                break
    except:
        print("This ATM is out of order.")
if __name__ == "__main__":
    print(__name__)
    savingsAccount()
