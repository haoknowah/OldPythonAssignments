def incomeTax():
    '''
determines how much tax must be paid based o your income
@param inc=income
@param tax=tax paid
    '''
    try:
        inc=float(input("Enter your taxable income: "))
        if inc <= 20000:
            tax=0.02*inc
        elif inc <= 50000:
            tax=400+(0.025*(inc-20000))
        else:
            tax=1150+(0.035*(inc-50000))
        print("Your tax is: $", tax, sep="")
    except:
        print("You never filed taxes, I should know, because I'm your computer.")

if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                incomeTax()
        main()
    except:
        print("The lights are on but no one is home.")
