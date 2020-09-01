def priceToEarningsRatio():
    '''
determines how much was made from purchasing a stock
@param x=stock price
@param y=annual income
@param nam=name that you choose
note that the inputs would not work when nam was used to insert company name into prompt
    '''
    try:
        nam=input("Enter the irrelevant name of your fictitious company: ")
        x=float(input("Enter the stock price: "))
        y=float(input("Now enter the anual income: "))
        print(nam, "'s price to earnings is: ",x/y, sep="")
    except:
        print("Loading...")
        
