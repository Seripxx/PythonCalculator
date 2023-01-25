import math
import tkinter as tk
window = tk.Tk()
#Sets the window size
window.geometry("500x70")
#Sets the window/program Name
window.title('Seripxx Calculator')

#Function for addition
def addition():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(font = 100,text="Result: " + str(result))

#Function for subtraction
def subtraction():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    result_label.config(font = 100,text="Result: " + str(result))

#Function for multiplication
def multiplication():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(font = 100,text="Result: " + str(result))    

#Function for division
def division():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 / num2
    result_label.config(font = 100, text="Result: " + str(result))  
      
#Function for clearing text fields.
def clear():
    result_label.config(font = 100, text = "Result:")
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')


#Addition button
add_button = tk.Button(window,width = 5,height=2, text="+", command=addition)
add_button.pack(side=tk.LEFT)

#Subtraction button
subtract_button = tk.Button(window,width = 5,height=2, text="-", command=subtraction)
subtract_button.pack(side=tk.LEFT)

#Multiplication button
add_button = tk.Button(window,width = 5,height=2, text="*", command=multiplication)
add_button.pack(side=tk.LEFT)

#dDivision Button
add_button = tk.Button(window,width = 5,height=2, text="/", command=division)
add_button.pack(side=tk.LEFT)

#Clear Button
add_button = tk.Button(window,width = 5,height=2, text="Clear", command=clear)
add_button.pack(side=tk.LEFT)

entry1 = tk.Entry(window, width = 50, font = 100)
entry1.pack(side=tk.TOP)
entry2 = tk.Entry(window, width = 50, font = 100)
entry2.pack(side=tk.TOP)
result_label = tk.Label(window,font = 100, text="Result: ")
result_label.pack()
window.mainloop()