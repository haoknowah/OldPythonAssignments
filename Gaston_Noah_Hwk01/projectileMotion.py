def projectileMotion():
    '''
hwk 1 problem 70
determines height of a ball after three seconds of launch
@param v=velocity
@param h1=starting height
@param t=time
@param h3=height after 3 seconds
    '''
    try:
        v=50
        h1=5
        t=3
        h3=-16*t**2+v*t+h1
        print(h3)
    except IOError:
        print("What else are you running that requires you to run this program.")
