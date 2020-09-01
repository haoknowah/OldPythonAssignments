def changeInSalary():
    '''
calculates the increase in salary
@param x=starting salary
@param y=new salary
@param z=percent increase
the except statement is a reference to dragon ball
    '''
    try:
        x=float(input("Enter your starting salary here: "))
        y=x*1.05*1.05*1.05
        print("New salary: $",round(y,2), sep="")
        z=(1.05**3-1)*100
        print("Percentage change: ",round(z,2), sep="", end="%")
    except:
        print("IT'S OVER 9000!!!")
if __name__=="__main__":
    '''
tests function changeInSalary()
    '''
    print(__name__)
    changeInSalary()
