def sameBirthday():
    '''
sameBirthday()=determines odds of people sharing a birthday in a group
formula=1-(n/n *(n-1)/n *... (n-x-1)/n)
@param x=number of people in group n=365
print odds of people sharing a birthday
    '''
    try:
        for num in range(21,25):
            formula=float(365/365)
            for x in range(num-1):
                formula=formula*((365-x-1)/365)
            formula=1-formula
            print("In a group of ",num, " people, the odds of two of them sharing a birthday is ",round(formula,3), sep="")
    except:
        print("Error.")
if __name__ == "__main__":
    print(__name__)
    sameBirthday()
