import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import load_data as data 
import events_handler as action

root = tk.Tk()
root.title("Forest")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)
# Import the tcl file
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')



# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=0, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Full name Label
full_name_label = ttk.Label(widgets_frame, text="Full Name")
full_name_label.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="w")
# Full name Entry
full_name_entry = ttk.Entry(widgets_frame)
full_name_entry.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")

# Education Label
education_label = ttk.Label(widgets_frame, text="Education")
education_label.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="w")
# Education Entry
education_entry = ttk.Entry(widgets_frame)
education_entry.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

# Graduation Label
graduation_label = ttk.Label(widgets_frame, text="Graduation year")
graduation_label.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="w")
# Education Entry
graduation_entry = ttk.Entry(widgets_frame)
graduation_entry.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")

# Years of Experience Label
years_of_exp_label = ttk.Label(widgets_frame, text="Years of Experience")
years_of_exp_label.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="w")
# Years of Experience Entry
years_of_exp_entry = ttk.Entry(widgets_frame)
years_of_exp_entry.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="ew")
years_of_exp_entry.config(validate="key", validatecommand=(root.register(action.validate_numeric_entry), "%P"))

# Automotive Experience Label
automative_exp_label = ttk.Label(widgets_frame, text="Automotive Experience")
automative_exp_label.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="w")
# Automotive Experience Entry
automative_exp_entry = ttk.Entry(widgets_frame)
automative_exp_entry.grid(row=4, column=1, padx=5, pady=(0, 10), sticky="ew")
automative_exp_entry.config(validate="key", validatecommand=(root.register(action.validate_numeric_entry), "%P"))

# Interviewer Label
interviewer_label = ttk.Label(widgets_frame, text="Interviewer name")
interviewer_label.grid(row=5, column=0, padx=5, pady=(0, 10), sticky="w")
# Interviewer Entry
interviewer_entry = ttk.Entry(widgets_frame)
interviewer_entry.grid(row=5, column=1, padx=5, pady=(0, 10), sticky="ew")

# Interview Date Label
interview_date_label = ttk.Label(widgets_frame, text="Interview Date")
interview_date_label.grid(row=6, column=0, padx=5, pady=(0, 10), sticky="w")
# Interview Date Entry
interview_date_entry = DateEntry(widgets_frame, date_pattern="yyyy-mm-dd")
interview_date_entry.grid(row=6, column=1, padx=5, pady=(0, 10), sticky="ew")

# Combobox avilability
availability_label = ttk.Label(widgets_frame, text="Availability")
availability_label.grid(row=7, column=0, padx=5, pady=(0, 10), sticky="w")
availability_list = data.get_availability_list()
availability_combobox = ttk.Combobox(widgets_frame, values=availability_list)
availability_combobox.current(1)
availability_combobox.grid(row=7, column=1, padx=5, pady=(0, 10), sticky="ew")

# Availability Check Date Label
availability_check_date_label = ttk.Label(widgets_frame, text="Availability Check Date")
availability_check_date_label.grid(row=8, column=0, padx=5, pady=(0, 10), sticky="w")
# Availability Check Date Entry
availability_check_date_entry = DateEntry(widgets_frame, date_pattern="yyyy-mm-dd")
availability_check_date_entry.grid(row=8, column=1, padx=5, pady=(0, 10), sticky="ew")

# Feedback Label
feedback_label = ttk.Label(widgets_frame, text="Feedback")
feedback_label.grid(row=9, column=0, padx=5, pady=(0, 10), sticky="w")
# Feedback Text Entry
feedback_text = tk.Text(widgets_frame, height=5, width= 50)
feedback_text.grid(row=9, column=1, padx=5, pady=(0, 10), sticky="ew")

# Comment Label
comment_label = ttk.Label(widgets_frame, text="Comment")
comment_label.grid(row=10, column=0, padx=5, pady=(0, 10), sticky="w")
# Comment Text Entry
comment_text = tk.Text(widgets_frame, height=5, width=50)
comment_text.grid(row=10, column=1, padx=5, pady=(0, 10), sticky="ew", columnspan=2)

# Consultants skills 
# widgets_frame.columnconfigure(0, weight=0)
check_frame = ttk.LabelFrame(root, text="Consultant Skills", height=50)
check_frame.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
checkbuttons_skill = []
for index, value in enumerate(data.get_consultant_skills()):
    a = tk.BooleanVar(value=False)
    check = ttk.Checkbutton(check_frame, text=value[1], variable=a)
    check.grid(row=index, column=0, padx=(5, 5), pady=10, sticky="nsew")
    checkbuttons_skill.append((check,a))
    
#group all entries in a dictionnary
entries = {
    "full_name": full_name_entry,
    "education": education_entry,
    "graduation_year":graduation_entry,
    "years_of_exp": years_of_exp_entry,
    "automative_exp": automative_exp_entry,
    "skills":checkbuttons_skill,

    "interviewer":interviewer_entry,
    "interview_date":interview_date_entry,
    "availability":availability_combobox,
    "availability_check_date": availability_check_date_entry,
    'feed_back': feedback_text,
    'comment': comment_text,

}


paned = ttk.PanedWindow(root)
paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2, 3, 4), height=12)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Treeview columns
treeview.column("#0", anchor="w", width=60)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)
treeview.column(3, anchor="w", width=120)
treeview.column(4, anchor="w", width=120)

# Treeview headings
treeview.heading("#0", text="Pos", anchor="w")
treeview.heading(1, text="Full name", anchor="w")
treeview.heading(2, text="Education", anchor="w")
treeview.heading(3, text="Years of exp", anchor="w")
treeview.heading(4, text="Automative exp", anchor="w")

# Define treeview data
_, treeview_data = data.get_consultants()

# Insert treeview data
for item in treeview_data:
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
    if item[0] == "" or item[2] in (8, 12):
        treeview.item(item[2], open=True) # Open parents

# Select and scroll
treeview.selection_set(0)
treeview.see(0)
# Bind event handler to row click event
treeview.bind("<<TreeviewSelect>>",lambda event: action.handle_row_click(event, treeview, entries))

#create a frame for buttons
action_frame = ttk.LabelFrame(root, text=" Action ", padding=(20, 10))
action_frame.grid(row=1, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
# add Button
add_button = ttk.Button(action_frame, text="Save consultant infos",style="Accent.TButton", command=lambda:action.add_data(treeview, entries))
add_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
# update Button
update_button = ttk.Button(action_frame, text="Update consultant infos",
                           command=lambda:action.update_data(treeview, entries))
update_button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
# delete Button 
delete_button = ttk.Button(action_frame, text="Remove consultant",
                          command=lambda:action.delete_data(treeview))
delete_button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")







# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Notebook
notebook = ttk.Notebook(pane_2)

# Tab #1
tab_1 = ttk.Frame(notebook)
tab_1.columnconfigure(index=0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0, weight=1)
tab_1.rowconfigure(index=1, weight=1)
notebook.add(tab_1, text="Search for consultant")

# Search area 
search_label = ttk.Label(tab_1, text="Search consultants by keyword ")
search_label.grid(row=0, column=0, padx=5, pady=(0, 20), sticky="w")  # Reduced pady to 2
search_entry = ttk.Entry(tab_1)
search_entry.grid(row=0, column=1, padx=5, pady=(0, 20), sticky="ew")  # Reduced pady to 2
search_entry.bind("<KeyRelease>", lambda event: action.filter_data(event, treeview, search_entry))




# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Tab 2")

# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Tab 3")

notebook.pack(expand=True, fill="both", padx=5, pady=5)

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Register the on_close function to be called when the window is closed
root.protocol("WM_DELETE_WINDOW", lambda: action.on_close(root))
# Start the main loop
root.mainloop()


