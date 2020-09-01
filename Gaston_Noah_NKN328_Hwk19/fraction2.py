class Fraction:
    def __init__(self, numerator=1, denominator=1, decimal=0.5):
        self.numerator=numerator
        self.denominator=denominator
        self.decimal=decimal
    def simplify(self):
            '''
determines what the greatest common divisor is for 2 integers
@param lis=list containing integers to help sort them, meaning that this could be expanded by adding more variables in
@param i=minimum number of the integers that could be used as a starting point to count down from
@param fraction=reduced fraction as a string
returns fraction
            '''
            try:
                lis=[int(self.numerator),int(self.denominator)]
                i=min(lis)
                if int(self.numerator)%i != 0 or int(self.denominator)%i != 0:
                    while int(self.numerator)%i!=0 or int(self.denominator)%i!=0:
                        i-=1
                self.numerator=int(self.numerator)/i
                self.denominator=int(self.denominator)/i
                fraction=str(round(self.numerator))+"/"+str(round(self.denominator))
                return fraction
            except:
                print("To infinity and beyond.")
    def convertToFraction(self):
        '''

        '''
        try:
            base=str(self.decimal.lstrip("0."))
            self.numerator=10**base * float(self.decimal)
            self.denominator=10**(len(str(self.decimal))-2)
        except:
            print("Unhandled exception in conversion.")
    def getDecimal(self):
        return self.decimal
