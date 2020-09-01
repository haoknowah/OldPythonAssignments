def profitFromStock():
    '''
hwk 1 problem 48
determine percent profit based on cost of item and how much it is sold for
    '''
    try:
        purchasePrice=10
        sellingPrice=15
        percentProfit=100*((sellingPrice-purchasePrice)/purchasePrice)
        print(percentProfit)
    except ZeroDivisionError:
        print("there is no zero or input, so if you are seeing this, there is something wrong with you.")
        
