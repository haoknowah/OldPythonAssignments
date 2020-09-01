def graduationHonors():
    '''
Also copied and modified from exercise 8
pretty much the same as the last one
    '''
    try:
        ## Bestow graduation honors.
        # Request grade point average.
        gpa = eval(input("Enter your gpa: "))
        if gpa >4 or gpa < 2:
            print("Try again cheater.")
        else:
            # Determine if honors are warranted.
            if gpa >= 3.9:
                honors = " summa cum laude."
            elif gpa >= 3.6:
                honors = " magna cum laude."
            elif gpa >= 3.3:
                honors = " cum laude."
            else:
                honors = "."
            # Display conclusion.
            print("You graduated" + honors)
    except:
        print("You were expelled.")
if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                graduationHonors()
        main()
    except:
        print("The lights are on but no one is home.")
