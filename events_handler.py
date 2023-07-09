from get_data import *
import tkinter as tk
from tkinter import messagebox

def handle_row_click(event, treeview, entries):
    selected_item = treeview.focus()
    clicked_row_index = treeview.index(selected_item)
    row = data[clicked_row_index]
    for index, entry in enumerate(entries):
        entry.delete(0, tk.END) 
        entry.insert(0,row[4][index])

def delete_data(clicked_row_index):
    response = messagebox.askyesno("Confirmation", "Are you sure you want to delete?")
    if response == True:
        global df
        df = df.drop(clicked_row_index)
        messagebox.showinfo("Information", "Operation completed successfully!")
    else:
        pass
    
