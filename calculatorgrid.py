import tkinter as tk
import tkinter.messagebox as mb

#Error handling needs return at the end to end the function otherwise it will loop the print and showerror command.
#Function for addition
def addition():
    while True:
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 + num2
            result_label.config(text="Result: " + str(result))
            break
        except ValueError as err:
            print("Please only enter numbers")
            mb.showerror(title="Error", message="Please only enter numbers")
            return

#Function for subtraction
def subtraction():
    while True:
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 - num2
            result_label.config(text="Result: " + str(result))
            break
        except ValueError as err:
            print("Please only enter numbers")
            mb.showerror(title="Error", message="Please only enter numbers")
            return

#Function for multiplication
def multiplication():
    while True:
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 * num2
            result_label.config(text="Result: " + str(result))
            break
        except ValueError as err:
            print("Please only enter numbers")
            mb.showerror(title="Error", message="Please only enter numbers")
            return
#Function for division
def division():
    while True:
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 / num2
            result_label.config(text="Result: " + str(result))  
            break
        except ZeroDivisionError as err:
            print("Handling run-time error:", err)
            mb.showerror(title="Error", message="Unable to divide by Zero",)
            return
        except ValueError as err:
            print("Please only enter numbers")
            mb.showerror(title="Error", message="Please only enter numbers",)
            return


#Function for clearing text fields.
def clear():
    result_label.config(text = "Result:")
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    return


window = tk.Tk()
window.title('Seripxx Calculator')


# Configure the rows and columns to have a non-zero weight
for i in range(4):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

# Create a frame to hold the entry fields
entry_frame = tk.Frame(window)
entry_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Create entry fields and add them to the entry frame
entry1 = tk.Entry(entry_frame)
entry1.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
entry2 = tk.Entry(entry_frame)
entry2.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Create buttons and add them to the button frame
add_button = tk.Button(button_frame, text="+", command=addition)
add_button.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
subtract_button = tk.Button(button_frame, text="-", command=subtraction)
subtract_button.grid(row=0, column = 1, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
multiply_button = tk.Button(button_frame, text="*", command=multiplication)
multiply_button.grid(row=0, column = 2, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
divide_button = tk.Button(button_frame, text="/", command=division)
divide_button.grid(row=0, column = 3, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

# Create a frame to hold the result label
result_frame = tk.Frame(window)
result_frame.grid(row=2, column=0, columnspan=4, sticky="nsew")

# Create result label and add it to the result frame
result_label = tk.Label(result_frame, text="Result: ")
result_label.grid(row=2, column=0, columnspan=4, sticky="nsew" )

#Create a frame to hold the clear button
clear_frame = tk.Frame(window)
clear_frame.grid(row=2, column=3, columnspan=4, sticky="nsew")
#Create a clear button and add it next to the clear frame.
clear_button = tk.Button(clear_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=0, columnspan=4, sticky="nsew")
window.mainloop()