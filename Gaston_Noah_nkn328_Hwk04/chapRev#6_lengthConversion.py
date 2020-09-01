def lengthConvertion():
    '''
converts the units of miles, yards, feet, and inches to kilometers, meters, and
centimeters
@param m=miles
@param y=yards
@param f=feet
@param i=inches
@param ti=total inches
@param tmeters=total meters
@param km=kilometers
@param meters=meters
@param cm=centimeters
Note the commentary, also I remember you mentioning something about documentation
using #, but I don't remember what it was. Are you going to create some sort of
master documentation template that shows how we need to document our programs
    '''
    try:
        m=int(input("Enter number of miles: "))
        y=int(input("Enter number of yards: "))
        f=int(input("Enter number of feet: "))
        i=int(input("Enter number of inches: "))
        print("Metric length: ")
        print("Hamster wheels going full power.")
        ti=63360*m+36*y+12*f+i
        tmeters=ti/39.37
        km=int(tmeters/1000)
        meters=int(tmeters%1000)
        cm=float(round(100*(tmeters%1), 1))
        print("Done. After conversion it is: ")
        print(km, "kilometers")
        print(meters, "meters")
        print(cm, "centimeters")
    except:
        print("Use Google.")
if __name__ =="__main__":
    print(__name__)
    lengthConvertion()
