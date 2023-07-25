import load_data as data 
import tkinter as tk
from tkinter import messagebox
import re
from tkcalendar import DateEntry
import pandas as pd 
from tkinter import ttk 


df, _ = data.get_consultants()

def validate_numeric_entry(entry):
    if re.match(r'^-?\d*\.?\d*$', entry) or entry == "":
        return True
    return False



def handle_row_click(event, treeview, entries):
    global df
    selected_item = treeview.focus()
    if not selected_item:
        return  
    clicked_row_index = treeview.index(selected_item)
    if clicked_row_index < len(df):
        row = df.iloc[clicked_row_index]
        for key, entry_widget in entries.items():
            if key == "skills":
                if row[key]:
                    skill_ids = [int(skill.strip()) for skill in row[key].split(",")]
                    skills = data.get_consultant_skills() 
                    filtered_skills = [skill[1] for skill in skills if skill[0] in skill_ids]
                    for checkbox, checkbox_var in entry_widget:
                        skill_name = checkbox.cget("text")
                        checkbox_var.set(skill_name in filtered_skills)

            elif isinstance(entry_widget, ttk.Combobox):
                entry_widget.set(row[key])
            elif isinstance(entry_widget, tk.Text):
                entry_widget.delete("1.0", tk.END)
                entry_widget.insert("1.0", row[key])
            elif isinstance(entry_widget, DateEntry):
                entry_widget.set_date(row[key])
            else:
                entry_widget.delete(0, tk.END)
                entry_widget.insert(0, row[key])


def filter_data(event, treeview, search_entry):
    keyword = search_entry.get().lower()
    def contains_keyword(values):
        return any(keyword in str(value).lower() for value in values)
    items = list(filter(lambda item: contains_keyword(treeview.item(item, 'values')), treeview.get_children()))
    for item in items:
        treeview.move(item, '', 0)


def delete_data(treeview):
    response = messagebox.askyesno("Confirmation", "Are you sure you want to delete?")
    if response == True:
        global df
        selected_item = treeview.focus()
        if selected_item:
            clicked_row_index = treeview.index(selected_item)
            treeview.delete(selected_item)
            df = df.drop(clicked_row_index)
            messagebox.showinfo("Information", "Operation completed successfully!")
        else:
            messagebox.showinfo("Information", "Select at least one consulatnt !")
    else:
        pass


def get_submitted_data(entries):
    new_row = {}
    for key, entry_widget in entries.items():
        if key == "skills":
            skill_ids = []
            skills = data.get_consultant_skills()
            for checkbox, checkbox_var in entry_widget:
                if checkbox_var.get():
                    skill_name = checkbox.cget("text")
                    skill_ids += [skill[0] for skill in skills if skill[1] == skill_name]
            skill_ids = ','.join(map(str, skill_ids))
            new_row[key] = skill_ids
        elif isinstance(entry_widget, tk.Text):
            new_row[key] = entry_widget.get("1.0", "end-1c")
        else:
            new_row[key] = entry_widget.get()
    
    return new_row


def add_data(treeview, entries):
    global df
    new_row = get_submitted_data(entries)
    df_row = pd.DataFrame(new_row, index=[0])
    df = pd.concat([df_row, df]).reset_index(drop=True)
    # adding the new row to the treeview  
    values = (new_row["full_name"], new_row["education"], new_row["years_of_exp"], new_row["automative_exp"])
    last_index = df.index[-1]
    new_index = last_index + 1
    item = ("", "0", new_index, 0, values)
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
    #Reset the indices of all rows in the Treeview
    for idx, item in enumerate(treeview.get_children()):
        treeview.item(item, text=idx)


def update_data(treeview,entries):
    selected_item = treeview.focus()
    if not selected_item:
        return 
    global df 
    new_row = get_submitted_data(entries)
    clicked_row_index = treeview.index(selected_item)
    print(clicked_row_index)
    df.loc[clicked_row_index] = new_row
    print(df.head(5))
    values = (new_row["full_name"], new_row["education"], new_row["years_of_exp"], new_row["automative_exp"])
    treeview.item(selected_item, values=values)


def on_close(root):
    global df 
    export_path = "data/consultants.csv"
    df.to_csv(export_path, index=False, sep='|')
    root.after(2000, root.destroy)



