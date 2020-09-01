def serversTip():
    '''
determines the amount needed for a server's tip
@param x=bill
@param t=tip percentage
    '''
    try:
        x=float(input("Enter the bill: "))
        t=float(input("Enter the percentage tip: "))
        print("The tip is $", x*(t/100), sep="")
    except:
        print("My tip is don't eat the yellow snow.")
