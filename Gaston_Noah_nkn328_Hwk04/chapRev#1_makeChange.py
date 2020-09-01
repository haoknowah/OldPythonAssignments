from tkinter import *
from tkinter import __init__
from tkinter.ttk import *
def makeChange():
    '''
determines the number of coins that you have in change
@param x=number of cents
@param s=Sackajewia coins
@param q=quarter coins
@param d=dime coins
@param n=nickel
@param p=penny coins

Note: the instructions said for the input to be only up to 99 cents, but I thought
that I should over achieve some, also note that nickel is the only coin without
a plural form, which is because no matter what, you will never get back more
than one of them in change since 2 nickels = 1 dime
    '''
    try:
        x=int(input("Enter an amount of change in cents: "))
        s=x//100
        q=(x-(s*100))//25
        d=(x-(s*100)-(q*25))//10
        n=(x%10)//5
        p=x%5
        print("Sackajewia(s):",s)
        print("Quarter(s):",q)
        print("Dime(s):",d)
        print("Nickel:",n)
        print("Penny(ies):",p)
    except:
        '''
        root=Tk()
        shennanigans=Button(root)
        abyss=PhotoImage(file='eareth.gif')
        shennanigans.image=abyss
        shennanigans.configure(image=abyss)
        root.mainloop()

        This part was supposed to make a little blank window pop up when the
        exception was called, but it looks like this only functions for when
        it is not part of the except statement, was trying to experiment with
        some things to make an image or gif appear, but while it seems to find
        the file, the window would just pop up blank. I included the gif image
        if you wanted to toy with it and see what I was talking about, the name
        is a play on how they pronounce Earth on Lilo and Stitch, E-are-th.
        '''
        print("I tried")
if __name__ == "__main__":
    print(__name__)
    makeChange()
