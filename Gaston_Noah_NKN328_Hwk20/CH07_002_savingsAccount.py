try:
    import savingAccount
except ImportError as exc:
    print(exc)
def savingsAccount():
    '''
creates and modifies a bank account
@param name=account name
@param newAccount=object of class savingAccount
@param action=action performed
@param deposit, withdrawal= amount used in action
prints the given information related to action performed
    '''
    try:
        name=input("Type name of account: ")
        newAccount=savingAccount.SavingsAccount(name)
        while True:
            action=input("D for deposit, W for withdrawal, B for current balance, "
                  "or Q to quit.")
            if action.upper()=="D":
                while True:
                    deposit=input("Enter amount to deposit in digits: ")
                    if deposit.isdigit==False:
                        print("Not a proper number.")
                    else:
                        break
                newAccount.makeDeposit(float(deposit))
                print("New balance is $", newAccount.getBalance(), sep="")
            elif action.upper()=="W":
                while True:
                    withdrawal=input("Enter amount to withdraw in digits: ")
                    if withdraw.isdigit==False:
                        print("Not a proper number.")
                    else:
                        break
                newAccount.makeWithdrawal(float(withdrawal))
                print("New balance is $", newAccount.getBalance(), sep="")
            elif action.upper()=="B":
                print("Current balance is $", newAccount.getBalance(), sep="")
            elif action.upper()=="Q":
                break
            else:
                print("Not an option.")
        print("Have a good day ", name, sep="")
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    try:
        savingsAccount()
    except:
        print("Unhandled exception.")
    
