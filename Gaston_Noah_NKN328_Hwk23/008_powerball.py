try:
    from tkinter import *
    import random
except ImportError as exc:
    print(exc)
def draw():
    '''
gets white and red balls from raffle
@param whiteBallNumbers=random set of 5 white balls
@param redBallNumbers=random red ball
    '''
    try:
        whiteBallNumbers=random.sample(w, 5)
        redBallNumbers=random.sample(r, 1)
        redBalls.set(tuple(redBallNumbers))
        whiteNum["text"]=whiteBallNumbers
    except:
        print("Unhandled exception in draw.")
try:
    '''
creates window that plays powerball raffle/lottery
@param w, r=variable holding all possible balls of given color
@param i=counter for number of balls
@param window=object of Tk
@param produce=button widget to generate raffle
@param white, red=label widget for given ball color
@param whiteNum=label widget displaying white balls obtained
@param redBalls=variable holding obtained red ball
@param redNum=readonly widget displaying obtained red ball
    '''
    global w
    global r
    global whiteBallNumber
    global redBallNumbers
    i=0
    w=[]
    r=[]
    while i<59:
        w.append(i)
        i+=1
    i=0
    while i<35:
        r.append(i)
        i+=1
    window=Tk()
    window.title("Powerball")
    produce=Button(window, text="Produce a Drawing", fg="red", command=draw)
    produce.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    white=Label(window, text="White balls:", fg="red")
    white.grid(row=1, column=1, padx=(20,2), pady=5, sticky=E)
    whiteNum=Label(window, bg="black", fg="white")
    whiteNum.grid(row=1, column=2, padx=(2,20), pady=5, sticky=W)
    red=Label(window, text="Red Balls:", fg="red")
    red.grid(row=2, column=1, padx=(5,2), pady=5, sticky=E)
    redBalls=StringVar()
    redNum=Entry(window, state="readonly", fg="red", width=2, textvariable=redBalls)
    redNum.grid(row=2, column=2, padx=(2,10), pady=5, sticky=W)
    window.mainloop()
except:
    print("Unhandled exception.")
