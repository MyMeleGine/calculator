import tkinter as tk
import requests
import random

# # Create the main application window
# def calculate():
#     problem = math_problem_entry.get()
#     if 

root = tk.Tk()
root.title("Calculator")
root.geometry("400x300")


label_prompt = tk.Label(root, text = "Variable 1")
label_prompt.pack()



math_problem_entry = tk.Entry(root, width=40)
math_problem_entry.pack()

label_prompt = tk.Label(root, text = "Variable 2")
label_prompt.pack()

math_problem_entry = tk.Entry(root, width=40)
math_problem_entry.pack()

solve_button = tk.Button(root, text='Enter', command= math_problem_entry)
solve_button.pack()

insert = tk.Listbox(root, width=50, height=10)
insert.pack()



root.mainloop()
