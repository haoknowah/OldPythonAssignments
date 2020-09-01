def presentValue():
    '''
determines what the original price of a present you have yet to get would be
@function rewind=determines the original price of the present using a formula
iCanSeeTheFuture is a reference to dragon ball abridged
dialga is the name of the pokemon god of time
added sarcasm because the way the question is asked, it sounds like it is asking you to see the future
    '''
    try:
        iCanSeeTheFuture=float(input("Enter future value here as well as the winning lottery numbers: "))
        rate=float(input("Enter the interest rate as a percent: "))
        dialga=float(input("Enter the number of years(you can include fractions of a year too): "))
        rewind=iCanSeeTheFuture/((1+(rate/100))**dialga)
        print("Present value: $",round(rewind, 2), sep="")
    except:
        print("I am sorry, but neither of us are psychic and can see the future")
if __name__=="__main__":
    print(__name__)
    presentValue()
