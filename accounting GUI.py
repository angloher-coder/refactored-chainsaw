import pandas as pd
from tkinter import *

# Initialize a DataFrame to store transactions
columns = ["Date", "Description", "Income", "Expense", "Balance"]
data = pd.DataFrame(columns=columns)

# Tkinter window
window = Tk()
window.title("Simple Accounting Software")

# Function to add transaction
def add_transaction():
    date = entry_date.get()
    desc = entry_desc.get()
    income = float(entry_income.get())
    expense = float(entry_expense.get())
    balance = income - expense

    # Append new transaction to the data
    new_data = pd.DataFrame([[date, desc, income, expense, balance]], columns=columns)
    global data
    data = data.append(new_data, ignore_index=True)

    # Clear the inputs
    entry_date.delete(0, END)
    entry_desc.delete(0, END)
    entry_income.delete(0, END)
    entry_expense.delete(0, END)

# GUI elements
Label(window, text="Date:").grid(row=0, column=0)
entry_date = Entry(window)
entry_date.grid(row=0, column=1)

Label(window, text="Description:").grid(row=1, column=0)
entry_desc = Entry(window)
entry_desc.grid(row=1, column=1)

Label(window, text="Income:").grid(row=2, column=0)
entry_income = Entry(window)
entry_income.grid(row=2, column=1)

Label(window, text="Expense:").grid(row=3, column=0)
entry_expense = Entry(window)
entry_expense.grid(row=3, column=1)

Button(window, text="Add Transaction", command=add_transaction).grid(row=4, column=0, columnspan=2)

# Start the GUI loop
window.mainloop()
