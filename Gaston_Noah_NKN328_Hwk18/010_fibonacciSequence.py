def fibonacciSequence(n, fib=[0,1]):
    '''
fibonacciSequence()=performs the fibonacci sequence using recursion and finds sum
@param n=input length of sequence
@param fib=list containing numbers of fibonacci sequence
@param number=sum of fibonacci sequence
returns number which is sum of fibonacci sequence
    '''
    try:
        if n<=2:
            number=sum(fib)
        else:
            n-=1
            number=fibonacciSequence(n, [fib[1],sum(fib)])
        return number
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_fibonacciSequence():
        '''
tests fibonacciSequence()
@param cont=determines if loop restarts
@param n=lenth of fibonacci sequence
prints sum of fibonacci sequence
        '''
        try:
            cont=True
            while cont==True:
                n=int(input("Type an integer here: "))
                print("Fibonacci number: ", fibonacciSequence(n))
                end=input("Reset? y or n ")
                if end.lower()=="n":
                    cont=False
        except ValueError:
            print("Not an int")
            end=input("Reset? y or n ")
            if end.lower()=="n":
                cont=False
        except:
                print("Unhandle exception.")
    test_fibonacciSequence()
