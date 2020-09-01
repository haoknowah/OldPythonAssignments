try:
    import turtle
except ImportError:
    print("You went slow but your aim wasn't steady.")
guys=[1375, 2047, 2233, 2559, 3265]
girls=[945, 2479, 3007, 3398, 4415]
def collegeEnrollment():
    '''
collegeEnrollment()=creates a line graph comparing the number of boys who went
to a 2 year college compared to girls in each year
@param squirtle=turtle object
@param line=calls line method to create axis for the graph
@param mysteriousTickingNoise=calls mysteriousTickingNoise method to create and
label ticks on the graph
@param notAStraightLine=calls notAStraightLine method to create dotted lines
for the genders
@param text=calls text method to create graph title
output is a graph showing men vs women in college
flair=squirtle is the name of a turtle pokemon as well as what I once named
my pet turtle, making it the perfect name for an object of class turtle
    '''
    try:
        squirtle=turtle.Turtle()
        line(squirtle, 0, 0, 250, 0)
        line(squirtle, 0, 0, 0, 175)
        mysteriousTickingNoise(squirtle)
        notAStraightLine(girls, squirtle)
        notAStraightLine(guys, squirtle)
        text(squirtle, 125, -30, "Two-Year College Enrollments")
        text(squirtle, 125, -45, "(in thousands)")
    except TypeError as exc:
        print(exc)
    except:
        print("Unhandled exception.")
    finally:
        squirtle.hideturtle()
def line(squirtle, x1, y1, x2, y2, color="black", dot=False):
    '''
line()=creates a line with turtle, either with dots or without
@param squirtle=turtle object
@param x1=starting x coordinate of line
@param y1=starting y coordinate of line
@param x2=ending x coordinate of line
@param y2=ending y coordinate of line
@param color=variable that determines color of line, default is black
@param dot=Boolean variable that determines if line will have dots at beginning
and end, default is False for no
output is single created line on graph
flair=final except statement is a pun off of the Chronicles of Narnia book titled
The Lion, the Witch, and the Wardrobe
    '''
    try:
        squirtle.pencolor(color)
        squirtle.up()
        squirtle.goto(x1, y1)
        if dot==True:
            squirtle.dot()
        squirtle.down()
        squirtle.goto(x2, y2)
        if dot==True:
            squirtle.dot()
    except TypeError as exc:
        print(exc)
    except:
        print("The Line, the Witch, and the Wardrobe.")
def mysteriousTickingNoise(squirtle):
    '''
mysteriousTickingNoise()=creates tick marks for the graph and labels it
@param squirtle=turtle object
@param i=variable used to count through items on list
@param maximum=the max number of students from both groups
@param minimum=the min number of students from both groups
output is the labeled frame of the graph
flair=named after the mysterious ticking noise song from Harry Potter Puppet Pals
    '''
    try:
        for i in range(len(girls)):
            line(squirtle, 40 * i+40, 0, 40 * i+40, 10)
            text(squirtle, 40*i+40, -20, 1970+10*i)
    except IndexError as exc:
        print(exc)
    try:
        maximum=0
        if max(guys)>max(girls):
            maximum=max(guys)
        else:
            maximum=max(girls)
        minimum=0
        if min(girls)<min(guys):
            minimum=min(girls)
        else:
            minimum=min(guys)
    except ValueError as exc:
        print(exc)
    try:
        line(squirtle, 0, maximum/30, 10, maximum/30)
        text(squirtle, -15, maximum/30, maximum)
        line(squirtle, 0, minimum/30, 10, minimum/30)
        text(squirtle, -15, minimum/30, minimum)
    except TypeError as exc:
        print(exc)
    except:
        print("Unhandled exception.")
def notAStraightLine(group, squirtle):
    '''
notAStraightLine()=creates chain of with dots for each number in list
@param group=what list was being drawn from, guys or girls
@param squirtle=turtle object
@param color=determines color of made line(s)
@param time=counts through the items in the list
output is a line with dots on graph showing change over time
flair=name is referencing the fact that it is making a line on a line graph when
a line is supposed to technically be completely straight
    '''
    try:
        if group==guys:
            color="blue"
        else:
            color="red"
    except:
        print("Unhandled exception.")
    try:
        for time in range(len(group)-1):
            line(squirtle, 40*time+40, group[time]/30, 40*(time+1)+40, group[time+1]/30, color, True)
    except IndexError as exc:
        print(exc)
    except:
        print("Unhandled exception.")
def text(squirtle, x, y, txt):
    '''
text()=creates text and puts it on graph
@param squirtle=turtle object
@param x=x coordinate of input text
@param y=y coordinate of input text
@param txt=text being input on graph
outputs a line of text on the graph
    '''
    try:
        squirtle.up()
        squirtle.pencolor("black")
        squirtle.goto(x,y)
        squirtle.write(txt, align="center")
    except ValueError as exc:
        print(exc)
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_collegeEnrollment():
        '''
tests the collegeEnrollment method
any exceptions should have been caught by this point, so no try blocks
        '''
        collegeEnrollment()
    test_collegeEnrollment()
