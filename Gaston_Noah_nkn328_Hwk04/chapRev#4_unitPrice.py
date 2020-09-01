def unitPrice():
    '''
determines the price per ounce of an object given its price with a weight of
pounds and ounces
@param x=final price
@param p=pounds
@param o=ounces
@paramy=price per ounce
Note: I made sure it was clear that user wasn't inputting same measurement twice
and that they know how to tell how many ounces are in a pound
    '''
    try:
        x=float(input("Enter the price of the item: "))
        p=float(input("Enter how many pounds it is rounded down to the nearest pound: "))
        o=float(input("Now enter how many ounces were rounded off (16 ounces in 1 pound): "))
        y=round(x/(p*16+o),2)
        print("The price per ounce is $",y, sep="")
    except:
        print("Would you like paper or plastic.")
if __name__ == "__main__":
    print(__name__)
    unitPrice()
        
