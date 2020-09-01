def marketingTerms():
    '''
finds the percentage markup and profit margin
@param x=selling price
@param y=purchase price
@param z=markup
    '''
    try:
        x=float(input("Enter the item's selling price: "))
        y=float(input("Enter the item's purchase price: "))
        z=x-y
        print("The item's percentage markup is $",z/y," and its profit margin is $",z/x, sep="")
    except:
        print("Enter the item's name:")
