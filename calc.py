import tkinter as tk

def add_variables():
 variable_1 = float(entry_1.get())
 variable_2 = float(entry_2.get())
 result = variable_1 + variable_2
 result_label.config(text=f"{result}")

def subtract_variables():
 variable_1 = float(entry_1.get())
 variable_2 = float(entry_2.get())
 result = variable_1 - variable_2
 result_label.config(text=f"{result}")

def multiply_variables():
 variable_1 = float(entry_1.get())
 variable_2 = float(entry_2.get())
 result = variable_1 * variable_2
 result_label.config(text=f"{result}")

def division_variables():
 variable_1 = float(entry_1.get())
 variable_2 = float(entry_2.get())
 result = variable_1 / variable_2
 result_label.config(text=f"{result}")

root = tk.Tk()
root.title("My Calculator")
root.geometry("400x300")

label_prompt_1 = tk.Label(root, text="Variable 1:")
label_prompt_1.pack()

entry_1 = tk.Entry(root, width=40)
entry_1.pack()

label_prompt_2 = tk.Label(root, text="Variable 2:")
label_prompt_2.pack()

entry_2 = tk.Entry(root, width=40)
entry_2.pack()

#Make plus and minus between each other in middle
middle_buttons = tk.Frame(root)
middle_buttons.pack(pady=10)

add_button = tk.Button(middle_buttons, text="+", command=add_variables)
add_button.pack(side=tk.LEFT, pady=20)

subtract_button = tk.Button(middle_buttons, text="-", command=subtract_variables)
subtract_button.pack(side=tk.RIGHT, pady=10)

multiply_button = tk.Button(middle_buttons, text="x", command=multiply_variables)
multiply_button.pack(side=tk.RIGHT, pady=10)

division_button = tk.Button(middle_buttons, text="%", command=division_variables)
division_button.pack(side=tk.RIGHT, pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
