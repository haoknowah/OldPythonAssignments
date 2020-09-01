try:
    import fraction
except ImportError as exc:
    print(exc)
def reduceAFraction():
    '''
reduceAFraction()=simplifies a fraction
@param numerator=fraction numerator
@param denominator=fraction denominator
@param reduction=object of class Fraction
@param reduced=simplified fraction
prints simplified fraction
    '''
    try:
        numerator=int(input("Input the numerator: "))
        while True:
            denominator=int(input("Input the denominator: "))
            if denominator==0:
                print("Can't divide by 0.")
            else:
                break
        reduction=fraction.Fraction(numerator, denominator)
        reduced=reduction.simplify()
        print(reduced)
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_reduceAFraction():
        '''
tests the reduceAFunction() method
@param cont=determines if loop restarts
        '''
        try:
            cont=True
            while cont==True:
                reduceAFraction()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Unhandled exception.")
    test_reduceAFraction()
