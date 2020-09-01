def populationGrowth():
    '''
hwk 1 problem 76
determine population growth
@param p200=population in 2000
@param p205=population in 2050
    '''
    try:
        p200=281
        p205=404
        percent=abs((p200-p205)/p200)*100
        print(round(percent,0))
    except ZeroDivisionError:
        print("We are not extinct.")
