class SavingsAccount:
    def __init__(self, name, balance=0):
        self.name=name
        self.balance=balance
    def makeDeposit(self, amount):
        '''

        '''
        try:
            self.balance=self.balance+amount
        except:
            print("Unhandled exception.")
    def makeWithdrawal(self, amount):
        '''

        '''
        try:
            if amount > self.balance:
                print("Not enough balance.")
            else:
                self.balance=self.balance-amount
        except:
            print("Unhandled exception.")
    def getBalance(self):
        return self.balance
    def __str__(self):
        return self.name + " has a balance of " + str(self.balance)
