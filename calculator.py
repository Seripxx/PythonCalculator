import math
import tkinter as tk
window = tk.Tk()
window.geometry("500x70")
window.title('Seripxx Calculator')
def addition():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(font = 100,text="Result: " + str(result))

def subtraction():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    result_label.config(font = 100,text="Result: " + str(result))

def multiplication():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(font = 100,text="Result: " + str(result))    

def division():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 / num2
    result_label.config(font = 100, text="Result: " + str(result))    


add_button = tk.Button(window,width = 5,height=2, text="+", command=addition)
add_button.pack(side=tk.LEFT)

subtract_button = tk.Button(window,width = 5,height=2, text="-", command=subtraction)
subtract_button.pack(side=tk.LEFT)

add_button = tk.Button(window,width = 5,height=2, text="*", command=multiplication)
add_button.pack(side=tk.LEFT)

add_button = tk.Button(window,width = 5,height=2, text="/", command=division)
add_button.pack(side=tk.LEFT)
entry1 = tk.Entry(window, width = 50, font = 100)
entry1.pack(side=tk.TOP)
entry2 = tk.Entry(window, width = 50, font = 100)
entry2.pack(side=tk.TOP)
result_label = tk.Label(window,font = 100, text="Result: ")
result_label.pack()
window.mainloop()





