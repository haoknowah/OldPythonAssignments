def costOfElectricity():
    '''
determines the electric bill from an appliance
@param x= energy usage
@param t=time used
@param y=the actual bill
    '''
    try:
        x=float(input("Enter how many kilowatts your device uses: "))
        t=float(input("Enter how long the device was used: "))
        y=(x*t)/(1000*11.76)
        print("The electricity bill will be: ",y)
    except:
        print("Just because my initials are NRG, don't think that you can blame your electric \
 bill on me.")
