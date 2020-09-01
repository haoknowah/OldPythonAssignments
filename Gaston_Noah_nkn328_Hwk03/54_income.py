def income():
    '''
calculates net income from revenue and expenses
degozaru is a japanese phrase that samurai are typically portrayed adding to the end of
their sentences and roughly translates to it is, so now it sounds like yoda speak
    '''
    try:
        revenue=float(input("Enter the company's annual revenue: "))
        expenses=float(input("Input the company's expenses: "))
        income=revenue-expenses
        print("For the net income, $",income, " ", sep="", end="degozaru")
    except:
        print("Wrong answer")
if __name__ == "__main__":
    '''
tests the method income
    '''
    print(__name__)
    income()
