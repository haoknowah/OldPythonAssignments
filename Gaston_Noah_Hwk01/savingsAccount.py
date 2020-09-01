def savingsAccount():
    '''
homework 1 problem 66
determines the rounded balance after 2 100 dolar deposits and 3 5%increases
@param balance=balance of acount
    '''
    try:
        balance=100
        balance=balance*1.05+100
        balance=balance*1.05+100
        balance=balance*1.05
        print(round(balance,2))
    except IOError:
        print("I don't care")
