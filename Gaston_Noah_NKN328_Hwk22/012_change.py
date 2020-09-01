try:
    from tkinter import *
except ImportError as exc:
    print(exc)
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
        x=amountInput.get()
        x=int(x)
        s.set(x//100)
        sackEntry["textvariable"]=s
        q.set((x-(int(sackEntry.get())*100))//25)
        quartersEntry["textvariable"]=q
        d.set((x-(int(sackEntry.get())*100)-(int(quartersEntry.get())*25))//10)
        dimesEntry["textvariable"]=d
        n.set((x-(int(sackEntry.get())*100)-(int(quartersEntry.get())*25)-(int(dimesEntry.get())*10))//5)
        nickelsEntry["textvariable"]=n
        p.set(x%5)
        penniesEntry["textvariable"]=p
        
    except:
        print("Unhandled exception in makeChange.")
'''
creates window that gives change
@param window=object of Tk
@param amount=label widget
@param amountInput=entry widget for amount of money
@param determine=button widget for calculations
@param sack, quarters, dimes, nickels, pennies=labels for appropriate coin types
@param sack/quarters/dimes/nickels/penniesEntry=displays amount of given coin
@param s, q, d, n, p=variables for amount of coins
'''
try:
    window=Tk()
    window.title("Change")
    amount=Label(window, text="Amount: ", fg="red")
    amount.grid(row=0, column=1, padx=5, pady=5, sticky=E)
    amountInput=Entry(window, fg="red", width=6)
    amountInput.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    determine=Button(window, text="Determine Composition of Change", fg="red", bg="black", command=makeChange)
    determine.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
    sack=Label(window, text="Sackajewia(s) ", fg="red")
    sack.grid(row=2, column=1, padx=5, pady=5, sticky=E)
    sackEntry=Entry(window, width=3, state="readonly", fg="gold")
    sackEntry.grid(row=2, column=2, padx=5, pady=5, sticky=W)
    quarters=Label(window, text="Quarter(s) ", fg="red")
    quarters.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    quartersEntry=Entry(window, state="readonly", width=2, fg="silver")
    quartersEntry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    dimes=Label(window, text="Dime(s): ", fg="red")
    dimes.grid(row=3, column=2, padx=5, pady=5, sticky=E)
    dimesEntry=Entry(window, state="readonly", width=2, fg="silver")
    dimesEntry.grid(row=3, column=3, padx=5, pady=5, sticky=W)
    nickels=Label(window, text="Nickel(s): ", fg="red")
    nickels.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    nickelsEntry=Entry(window, state="readonly", width=2, fg="silver")
    nickelsEntry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    pennies=Label(window, text="Penny(ies): ", fg="red")
    pennies.grid(row=4, column=2, padx=5, pady=5, sticky=E)
    penniesEntry=Entry(window, state="readonly", fg="brown", width=2)
    penniesEntry.grid(row=4, column=3, padx=5, pady=5, sticky=W)
    global s
    global q
    global d
    global n
    global p
    s=StringVar()
    q=StringVar()
    d=StringVar()
    n=StringVar()
    p=StringVar()
    window.mainloop()
except:
    print("Unhandled exception.")
