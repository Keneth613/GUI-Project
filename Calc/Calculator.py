from Tkinter import *
root = Tk()
height=3
width=5

def pressed7():
    global button_pressed
    editor.insert(END, str(7 ))
    
def pressed4():
    global button_pressed
    editor.insert(END, str(4 ))
    
def pressed1():
    global button_pressed
    editor.insert(END, str(1 ))
    
def pressed0():
    global button_pressed
    editor.insert(END, str(0 ))
    
def pressed2():
    global button_pressed
    editor.insert(END, str(2 ))
    
def pressed5():
    global button_pressed
    editor.insert(END, str(5 ))
    
def pressed8():
    global button_pressed
    editor.insert(END, str(8 ))
    
def pressed9():
    global button_pressed
    editor.insert(END, str(9 ))
    
def pressed6():
    global button_pressed
    editor.insert(END, str(6 ))
    
def pressed3():
    global button_pressed
    editor.insert(END, str(3 ))
     
def pressedPlus():
    global button_pressed
    editor.insert(END, str('+'))
    
def pressedEqual():
    global Equal
    editor.insert(END, str('='))            

def pressedDivision():
    global button_pressed
    editor.insert(END, str('%'))
    
def pressedMinus():
    global button_pressed
    editor.insert(END, str('-'))
    
def pressedDecimal():
    global button_pressed
    editor.insert(END, str('.'))
    
def pressedMultiply():
    global Multiply
    editor.insert(END, str('x'))   

def pressedClear():
    global Clear
    editor.delete(0,END)
    
button7 = Button(root, text='7', 
                command=pressed7)
button7.grid(row=0, column=0)

button7.config(height=height,width=width)

button4 = Button(root, text='4', 
                command=pressed4)
button4.grid(row=1, column=0)

button4.config(height=height,width=width)

button1 = Button(root, text='1', 
                command=pressed1)
button1.grid(row=2, column=0)

button1.config(height=height,width=width)

button0 = Button(root, text='0', 
                command=pressed0)
button0.grid(row=3, column=0)

button0.config(height=height,width=width)

button8 = Button(root, text='8', 
                command=pressed8)
button8.grid(row=0, column=1)

button8.config(height=height,width=width)

button5 = Button(root, text='5', 
                command=pressed5)
button5.grid(row=1, column=1)

button5.config(height=height,width=width)

button2 = Button(root, text='2', 
                command=pressed2)
button2.grid(row=2, column=1)

button2.config(height=height,width=width)

buttonDecimal = Button(root, text='.', 
                command=pressedDecimal)
buttonDecimal.grid(row=3, column=1)

buttonDecimal.config(height=height,width=width)

button9 = Button(root, text='9', 
                command=pressed9)
button9.grid(row=0, column=2)

button9.config(height=height,width=width)

button6= Button(root, text='6', 
                command=pressed6)
button6.grid(row=1, column=2)

button6.config(height=height,width=width)

button3 = Button(root, text='3', 
                command=pressed3)
button3.grid(row=2, column=2)

button3.config(height=height,width=width)

buttonEqual = Button(root, text='=', 
                command=pressedEqual)
buttonEqual.grid(row=3, column=2)

buttonEqual.config(height=height,width=width)

buttonPlus = Button(root, text='+', 
                command=pressedPlus)
buttonPlus.grid(row=0, column=3)

buttonPlus.config(height=height,width=width)

buttonMinus = Button(root, text='-', 
                command=pressedMinus)
buttonMinus.grid(row=1, column=3)

buttonMinus.config(height=height,width=width)

buttonDivision = Button(root, text='%', 
                command=pressedDivision)
buttonDivision.grid(row=2, column=3)

buttonDivision.config(height=height,width=width)

buttonMultiply = Button(root, text='x', 
                command=pressedMultiply)
buttonMultiply.grid(row=3, column=3)

buttonMultiply.config(height=height,width=width)

buttonClear = Button(root, text='Clear', 
                command=pressedClear)
buttonClear.grid(row=4, column=0,columnspan=4)

buttonClear.config(height=3,width=30)

editor = Text(width=30, height=5, font=("Times New Roman", 10))
editor.grid(row=5, column=0, columnspan=4)

root.mainloop()