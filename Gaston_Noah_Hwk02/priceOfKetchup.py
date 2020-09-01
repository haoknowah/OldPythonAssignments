def priceOfKetchup():
    '''
determines the price of ketchup during a sale
    '''
    try:
        item="ketchup"
        regularPrice=1.80
        discount=0.27
        print(float(regularPrice-discount), "is the sale price of", str(item))
    except:
        print("The ad that had this sale was for last year.")
