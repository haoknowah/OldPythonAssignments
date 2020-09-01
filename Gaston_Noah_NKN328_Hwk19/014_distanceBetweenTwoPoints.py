try:
    import point
except ImportError as exc:
    print(exc)
def distanceBetweenTwoPoints():
    '''
distanceBetweenTwoPoints()=determines the distance between two points on a plane
@param x1, y1, x2, y2=x and y coordinates of points
@param p=object holding point class
returns distance between two points
    '''
    try:
        x1=float(input("Enter x-coordinate of first point: "))
        y1=float(input("Enter y-coordinate of first point: "))
        x2=float(input("Enter x-coordinate of second point: "))
        y2=float(input("Enter y-coordinate of second point: "))
        #next line finds difference in x coordinates and y coordinates to make a
        #single point to use as method finds distance between one point and
        #origin which is the same as the distance would be between the 2 points
        p=point.Point(x1-x2, y1-y2)
        return p.distanceFromOrigin()
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_distanceBetweenTwoPoints():
        '''
tests distanceBetweenTwoPoints() method
@param cont=determines if loop restarts
        '''
        try:
            cont=True
            while cont==True:
                print(float(round(distanceBetweenTwoPoints(), 2)))
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Unhandled exception.")
    test_distanceBetweenTwoPoints()

    '''
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def distanceFromOrigin(self):
        return (self._x ** 2 + self._y ** 2) ** .5
    '''
    
