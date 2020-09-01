try:
    from tkinter import *
except ImportError as exc:
    print(exc)
def addNum():
    '''
adds numbers in entry boxes
@param numSum=sum of firstNum and secondNum
    '''
    try:
        numSum=float(firstNum.get())+float(secondNum.get())
        answerVar.set("Sum:"+str(numSum))
    except:
        print("Unhandled exception in addNum.")
def subtractNum():
    '''
subtract numbers in two entry boxes
@param numDif=difference between firstNum and secondNum
    '''
    try:
        numDif=float(firstNum.get())-float(secondNum.get())
        answerVar.set("Difference:"+str(numDif))
    except:
        print("Unhandled exception in subtractNum.")
def multiplyNum():
    '''
multiplies numbers in entry boxes
@param numProduct=product of firstNum and secondNum
    '''
    try:
        numProduct=float(firstNum.get())*float(secondNum.get())
        answerVar.set("Product:"+str(numProduct))
    except:
        print("Unhandled exception in multiplyNum.")
try:
    '''
creates window to act as calculator
@param window=object of Tk
@param first, second=labels for number inputs
@param first/secondEntry=entry widgets for respective numbers
@param first/secondNum=variable for relevant number
@param add, subtract, multiply=button widget for appropriate function
@param answerVar=variable holding answer
@param answer=readonly widget dispalying answerVar
    '''
    window=Tk()
    window.title("Calculator")
    first=Label(window, fg="red", text="First\nNumber:")
    first.grid(row=0, column=0, padx=5, pady=5)
    firstNum=StringVar()
    firstEntry=Entry(window, fg="red", width=5, textvariable=firstNum)
    firstEntry.grid(row=1, column=0, padx=5, pady=5)
    second=Label(window, fg="red", text="Second\nNumber:")
    second.grid(row=0, column=2, padx=5, pady=5)
    secondNum=StringVar()
    secondEntry=Entry(window, fg="red", width=5, textvariable=secondNum)
    secondEntry.grid(row=1, column=2, padx=5, pady=5)
    add=Button(window, fg="red", text="+", command=addNum)
    add.grid(row=0, column=1, padx=5, pady=5)
    subtract=Button(window, fg="red", text="-", command=subtractNum)
    subtract.grid(row=1, column=1, padx=5, pady=5)
    multiply=Button(window, fg="red", text="x", command=multiplyNum)
    multiply.grid(row=2, column=1, padx=5, pady=5)
    answerVar=StringVar()
    answer=Entry(window, state="readonly", fg="red", textvariable=answerVar)
    answer.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
    window.mainloop()
except:
    print("Unhandled exception.")
