try:
    import fraction
except ImportError as exc:
    print(exc)
def convertADecimalToAFraction():
    '''
convertADecimalToAFraction()=does exactly what its name implies
@param decimal=input decimal to be converted
@param convertion=object holding fraction class
@param converted=decimal converted into a fraction
prints decimal converted to fraction
    '''
    try:
        while True:
            decimal=float(input("Enter a decimal greater than zero but less than one: "))
            if decimal <=0 or decimal >= 1:
                print("Improper number.")
            else:
                break
        convertion=fraction.Fraction(5, 10, decimal)
        convertion.convertToFraction()
        converted=convertion.simplify()
        print(converted)
    except NameError as exc:
        print(exc)
    except:
        print("Unhandled exception.")
        
if __name__=="__main__":
    def test_convertADecimalToAFraction():
        '''
tests convertADecimalToAFraction() method
@param cont=determines if loop repeats
        '''
        try:
            cont=True
            while cont==True:
                convertADecimalToAFraction()
                end=input("Do you wish to continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Unhandled exception.")
    test_convertADecimalToAFraction()
