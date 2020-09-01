def gasMileage():
    '''
hwk problem 72
determines average number of miles per gallon
@param mi=initial mileage
@param mf=ending mileage
@param g=galons used
@param av=average
    '''
    try:
        mi=23352
        mf=23695
        g=14
        av=(mf-mi)/g
        print(av)
    except ZeroDivisionError:
        print("unless you were pushing the car so as to not use gas, you're wrong")
