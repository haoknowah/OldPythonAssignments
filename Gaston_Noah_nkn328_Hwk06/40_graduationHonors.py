def graduationHonors():
    '''
copied from exercise 8 as it said and then modified it
kept els statements in there so that the print part would remain outside of the loops and thus go off for any of them
    '''
    try:
        ## Bestow graduation honors.
        # Request grade point average.
        gpa = eval(input("Enter your gpa: "))
        # Determine if honors are warranted.
        if gpa >= 3.9:
            honors = " summa cum laude."
        else:
            if gpa >= 3.6:
                honors = " magna cum laude."
            else:
                if gpa >= 3.3:
                    honors = " cum laude."
                else:
                    honors = "."
        # Display conclusion.
        print("You graduated" + honors)
    except:
        print("You flunked out of college.")

if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                graduationHonors()
        main()
    except:
        print("The lights are on but no one is home.")
