def stockPurchase():
    '''
finds and shows the how much is spent on shares
    '''
    try:
        costPerShare=25.625
        numberOfShares=400
        amount=costPerShare*numberOfShares
        print(amount)
    except:
        print("Meow")
