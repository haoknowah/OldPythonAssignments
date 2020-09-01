def the12DaysOfChristmas():
    '''
the12DaysOfChristmas=asks for a number and determines the price from that many
days of the 12 days of Christmas stored in Gifts.txt
@param number=number of days specified
@param infile=contains file Gifts.txt
@param theDays=list holding the 12 days of Christmas from infile
@param day=day of theDays being checked
@param needed=list containing only the number of days used
@param subtotal=total cost of last day
@param total=total cost of all the days
prints what was done on what days and the cost of the last day as well as the
overall cost
    '''
    try:
        while True:
            number=input("Enter an integer 1 through 12: ")
            if number.isdigit()==False:
                print("Wrong")
            elif int(number) < 1 or int(number) > 12:
                print("Wrong size.")
            else:
                break
        infile=open("Gifts.txt", 'r')
        print("READ")
        theDays=[line.rstrip() for line in infile]
        infile.close()
        for day in range(len(theDays)):
            theDays[day]=theDays[day].split(",")
            theDays[day][0]=int(theDays[day][0])
            theDays[day][2]=float(theDays[day][2])
        needed=[]
        for day in range(len(theDays)):
            if int(theDays[day][0]) <= int(number):
                needed.append(theDays[day])
        print("The gifts for day ", number, " are: ", sep="")
        subtotal=0
        total=0
        for day in range(len(needed)):
            print("{0:<5n}{1:10s}".format(needed[day][0], needed[day][1]))
            subtotal=subtotal+(1+day)*needed[day][2]
            total=total+subtotal
        print("The cost for day ", number, " is: $", round(subtotal, 2), sep="")
        print("The total cost by day ", number, " is: $", round(total, 2), sep="")
    except:
        print("Error in the12DaysOfChristmas")
if __name__ == "__main__":
    def test_the12DaysOfChristmas():
        '''
test_the12DaysOfChristmas()=tests the the12DaysOfChristmas() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                the12DaysOfChristmas()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_the12DaysOfChristmas()
