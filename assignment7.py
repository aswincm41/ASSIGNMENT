#GUI

#QS1
import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    new_text = current_text + button_text
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 20), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(root, text=button_text, width=4, height=2, command=lambda text=button_text: on_click(text)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', width=4, height=2, command=clear_entry).grid(row=row_val, column=0)
tk.Button(root, text='=', width=4, height=2, command=calculate).grid(row=row_val, column=1, columnspan=3)

root.mainloop()


#QS2

import tkinter as tk

def print_data():
    user_input = entry.get()
    text_area.insert(tk.END, user_input + '\n')
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("User Input Printer")


entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)


print_button = tk.Button(root, text="Print Data", command=print_data)
print_button.grid(row=1, column=0, pady=10)

text_area = tk.Text(root, width=30, height=10)
text_area.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()

#QS3


import tkinter as tk

root = tk.Tk()
root.title("Label Configuration")
label = tk.Label(root, text="Hello, Tkinter!", bg="red", font=("Times New Roman", 18))
label.pack(pady=20)

root.mainloop()
