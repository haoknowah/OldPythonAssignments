try:
    from tkinter import *
    from num2words import num2words
except ImportError as exc:
    print(exc)
def verbalizeNumber():
    '''
verbalizeNumber=turns an input number into word form
@param x=input number being verbalized
@param numList=list of numbers in word form
    '''
    try:
        x=num2words(number.get())
        numList=x.split(",")
        verbalized.set(tuple(numList))
    except:
        print("Unhandled exception in verbalizeNumber.")
'''
creates window that displays a verbalized number
@param window=object of Tk
@param upperLabel, lowerLabel=label widgets
@param number=entry widget
@param verb=button widget
@param verbalized=list for listbox
@param numberList=listbox widget
'''
try:
    window=Tk()
    window.title("Verbalize")
    upperLabel=Label(window, text="Enter a number having at most", fg="red")
    upperLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    lowerLabel=Label(window, text="27 digits (including commas): ", fg="red")
    lowerLabel.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    number=Entry(window, fg="red", width=30)
    number.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    verb=Button(window, text="Verbalize Number", fg="red", bg="black", command=verbalizeNumber)
    verb.grid(row=3, column=0, padx=5, pady=5)
    verbalized=StringVar()
    numberList=Listbox(window, fg="red", width=50, height=10, listvariable=verbalized)
    numberList.grid(row=3, column=1, padx=5, pady=5)
    window.mainloop()
except:
    print("Unhandled exception.")
