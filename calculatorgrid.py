import math
import tkinter as tk
window = tk.Tk()
#Sets the window size
window.geometry("500x70")
#Sets the window/program Name
window.title('Seripxx Calculator')


bottom_frame = tk.Frame(window,width = 50, height =50, bg='grey')
bottom_frame.grid(row=2, column=0)
result_bar = tk.Frame(bottom_frame, width= 20, height = 20, bg='white')
result_bar.grid(row=0, column=0)
tk.Label(result_bar, text="Result:").grid(row=1, column=0, padx=0)

left_frame = tk.Frame(window, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=0, pady=0)

right_frame = tk.Frame(window, width=650, height=50, bg='grey')
right_frame.grid(row=0, column=1, padx=0, pady=0)

tool_bar = tk.Frame(left_frame, width=100, height=200)
tool_bar.grid(row=0, column=0, padx=8, pady=5)
tk.Button(tool_bar, text="+", relief=tk.RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
tk.Button(tool_bar, text="-", relief=tk.RAISED).grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
tk.Button(tool_bar, text="/", relief=tk.RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
tk.Button(tool_bar, text="*", relief=tk.RAISED).grid(row=1, column=1, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

entry_text = tk.Frame(right_frame, width=0, height = 0, bg ='grey')
entry_text.grid(row=0, column = 0)
tk.Entry(entry_text, text="", relief=tk.SUNKEN).grid(row=0, column=0, padx=10, pady=10, ipadx=10)  # ipadx is padding inside the Label widget
tk.Entry(entry_text, text="", relief=tk.SUNKEN).grid(row=1, column=0, padx=10, pady=10, ipadx=10)  # ipadx is padding inside the Label widget
window.mainloop()