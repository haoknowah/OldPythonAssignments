try:
    from tkinter import *
except ImportError as exc:
    print(exc)
'''
creates window displaying investing informatio, nonfunctional
@param window=object of Tk
@param invest=label containing amount invested
@param rate, period=labels stating said information
@param rate/periodList=list object for listbox containing relevant information
@param rate/periodListBox=listbox widget containing relevant list
@param calc=button widget
@param acrued=label for amount
@param entry=string for amount gained
@param amount=ReadOnly type Entry widget
'''
try:
    window=Tk()
    window.title("Investment")
    invest=Label(window, text="Invest $10,000", fg="red")
    invest.grid(row=0, column=1, padx=5, pady=5)
    rate=Label(window, text="Interest\nrate:", fg="red")
    rate.grid(row=1, column=0, padx=5, pady=5)
    period=Label(window, text="Compound\nperiods:", fg="red")
    period.grid(row=1, column=1, padx=5, pady=5)
    rateList=StringVar()
    rateListBox=Listbox(window, height=5, width=4, fg="red", listvariable=rateList)
    rateListBox.grid(row=2, column=0, padx=5, pady=5)
    rateList.set(tuple(["2%", "2.5%", "3%", "3.5%", "4%"]))
    periodList=StringVar()
    periodListBox=Listbox(window, height=5, fg="red", listvariable=periodList)
    periodListBox.grid(row=2, column=1, padx=5, pady=5)
    periodList.set(tuple(["anually", "semi-anually", "quarterly", "monthly", "weekly"]))
    calc=Button(window, text="Calculate\nAmount\nAfter 5\nYears", fg="red", bg="black")
    calc.grid(row=2, column=2, padx=5, pady=5)
    acrued=Label(window, text="Amount after 5 years: ", fg="red")
    acrued.grid(row=3, column=1, padx=5, pady=5, sticky=E)
    entry=StringVar()
    entry.set("$11,327.08")
    amount=Entry(window, state="readonly", fg="red", width=10, textvariable=entry)
    amount.grid(row=3, column=2, padx=5, pady=5)
    window.mainloop()
except:
    print("Unhandled exception.")
