def calories():
    '''
determines how many calories are in a cubic mile of chocolate ice cream
1.472*10**11 is number of cubic feet per cubic mile
    '''
    try:
        cal=48600
        total=(1.472*10**11)*cal
        print(total)
    except:
        print("Brain freeze")
