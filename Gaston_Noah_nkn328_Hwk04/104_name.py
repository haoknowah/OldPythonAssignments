def name():
    '''
determines what your middle name is when given your first, middle, and last names in order
@param x=full name
@param mid=list with the parts of your name
    '''
    try:
        x=input("Enter a three part name: ")
        mid=x.split(" ")
        print("Your middle name is ",mid[1], sep="")
    except:
        print("Would you like fries with that Mr. ____")
if __name__ == "__main__":
    print(__name__)
    name()
