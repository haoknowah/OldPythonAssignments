def income():
    '''
calculates net income from revenue and expenses
degozaru is a japanese phrase that samurai are typically portrayed adding to the end of
their sentences and roughly translates to it is, so now it sounds like yoda speak
    '''
    try:
        revenue=input(float("Enter the company's annual revenue: "))
        expenses=input(float("Input the company's expenses: "))
        print("For the net income, $",revenue-expenses, sep=""," ",end="degozaru")
    except:
        print("Wrong answer")
if__name__=="__main__":
    '''
tests the method income
    '''
    print(__name__)
    income()
