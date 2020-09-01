try:
    import fraction
except ImportError as exc:
    print(exc)
def addFractions():
    '''
addFractions()=adds two fractions together
@param numerator, denmoinator, numerator2, denominator2=numerators and denominators
of the fractions
@param balor=object holding fractions
@param added=sum of the two fractions
prints sum of two fractions
    '''
    try:
        numerator=int(input("Enter the numerator for the first fraction: "))
        denominator=int(input("Enter the denominator of the first fraction: "))
        numerator2=int(input("Enter the numerator of the second fraction: "))
        denominator2=int(input("Enter the denominator for the second fraction: "))
        balor=fraction.Fraction(numerator, denominator, 0, numerator2, denominator2)
        balor.addFractions()
        added=balor.simplify()
        print(numerator,"/",denominator," + ",numerator2,"/",denominator2,
              "=", added, sep="")
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_addFractions():
        '''
tests the addFractions method
@param cont=determines if loop repeats
        '''
        try:
            cont=True
            while cont==True:
                addFractions()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Unhandled exception.")
    test_addFractions()
