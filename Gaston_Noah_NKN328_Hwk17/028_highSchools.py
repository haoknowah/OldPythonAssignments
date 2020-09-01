try:
    import turtle
except ImportError:
    print("You went slow, but your aim wasn't steady.")
def highSchools():
    '''
highSchools()=creates a bar graph showing what type of high school college
freshman went to
@param squirtle=turtle object
@param start=where turtle will start drawing
@param height=height of box to be made
@param width=width of box to be made
@param first=text for first box
@param first2=second part of text
@param firstPercent=percentag first box covers
@param second=text for second box
@param secondPercent=percent second box covers
@param third=text for third box
@param thirdPercent=percent covered by third box
outputs a bar graph comparing percentages
flair=squirtle is the name of a turtle pokemon as well as what I once named
my pet turtle, making it the perfect name for an object of class turtle
    '''
    try:
        squirtle=turtle.Turtle()
        squirtle.pencolor("black")
        squirtle.up()
        start=-135
        squirtle.goto(start, 0)
        height=int(753/2)
        width=90
        start=box(height, width, start, squirtle)
        first="Public (not"
        first2="charter or magnet)"
        firstPercent="75.3%"
        second="Private"
        secondPercent="17.2%"
        third="Other"
        thirdPercent="7%"
        text(first, start, width, height, squirtle, first2, firstPercent)
        height=int(172/2)
        start=box(height, width, start, squirtle)
        text(second, start, width, height, squirtle, secondPercent)
        height=int(7/2)
        start=box(height, width, start, squirtle)
        text(third, start, width, height, squirtle, thirdPercent)
        squirtle.goto(0, -20)
        squirtle.write("Type of High School Attended by Fall 2013 College Freshman", align="center")
    except TypeError as exc:
        print(exc)
    except:
        print("Unhandled exception meow.")
    finally:
        squirtle.hideturtle()
def text(data, start, width, height, squirtle, data2="", percent=""):
    '''
text()=creates text to put on the graph
@param data=text being added
@param data2=second line of text added in case of two lines
@param start=bottom right corner of box that needs text
@param width=width of said box
@param height=height of said box
@param squirtle=turtle object
@param percent=whether or not text is percentage to be put on top of box
outputs text onto bar graph
    '''
    try:
        squirtle.goto(start-(width/2), 20)
        squirtle.write(data, align="center")
        if data2 != "":
            squirtle.goto(start-(width/2), 10)
            squirtle.write(data2, align="center")
        if percent != "":
            squirtle.goto(start-(width/2), height)
            squirtle.write(percent, align="center")
        squirtle.goto(start, 0)
    except TypeError as exc:
        print(exc)
    except:
        print("Unhandled exception.")
def box(height, width, start, squirtle):
    '''
box()=creates filled box on bar graph
@param height=height of created box
@param width=width of created box
@param sart=starting point of box
@param squirtle=turtle object
outputs box onto bar graph
    '''
    try:
        squirtle.fillcolor("red")
        squirtle.down()
        squirtle.begin_fill()
        squirtle.goto(start+width, 0)
        squirtle.goto(start+width, height)
        squirtle.goto(start, height)
        squirtle.goto(start, 0)
        squirtle.up()
        squirtle.end_fill()
        squirtle.goto(start+width, 0)
        start=start+width
        return start
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_highSchools():
        '''
tests highSchools method
all try and excepts are in other methods so there is no need for them here
        '''
        highSchools()
    test_highSchools()
