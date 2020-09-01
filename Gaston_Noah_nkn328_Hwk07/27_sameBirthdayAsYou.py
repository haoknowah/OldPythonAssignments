def sameBirthdayAsYou():
    '''
determines how many students need to be in the class for there to be more than a 50% chance of one of them sharing a birthday with you
@param n=number of students needed
    '''
    try:
        n=0
        while (364/365)**n > 0.5:
            n+=1
        print("There needs to be at least ",n," students in the class for there to be more than a 50% chance of someone sharing a birthday with you.",sep="")
    except:
        print("This is 100% if your twin is in the class.")

if __name__ == "__main__":
    print(__name__)
    sameBirthdayAsYou()
