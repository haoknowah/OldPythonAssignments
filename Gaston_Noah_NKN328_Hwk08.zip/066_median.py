import statistics
def median():
    '''
median()=finds median of list of numbers
I know that we haven't gone over this in class, but trying to do it with for
loops was proving to be impossible, so I implemented it this way, plus its neater
@param n=length of list
@param mocs=list of numbers
uses median method of statistics class to find median
print median
    '''
    try:
        n=int(input("Enter a number of values to input: "))
        mocs=[]
        for num in range(n):
            numb=int(input("Enter an integer here: "))
            mocs.append(numb)
        mocs.sort()
        print(statistics.median(mocs))
    except:
        print("Internal hamster wheel jammed.")
if __name__ == "__main__":
    print(__name__)
    median()
            
