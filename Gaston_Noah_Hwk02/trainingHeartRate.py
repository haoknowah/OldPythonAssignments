def trainingHeartRate():
    '''
determines what heart rate a person should have when exercising
@param a=age
@param r=resting heart rate
    '''
    try:
        a=float(input("What is your age: "))
        r=float(input("What is your resting heartrate: "))
        print("Your training heart rate is ", 0.7*(220-a)+(0.3*r))
    except:
        print("Undead can not measure their heart rate.")
        
