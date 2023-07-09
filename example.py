
import tkinter as tk
from tkinter import ttk
from get_data import data
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

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-light')

# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()

# Create a Frame for the Checkbuttons
check_frame = ttk.LabelFrame(root, text="Checkbuttons", padding=(20, 10))
check_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Checkbuttons
# Checkbuttons for consultant skills
checkbuttons_skill = [] 
constrol_vars = []
for index,value in enumerate(range(10)):
    a = tk.BooleanVar(value=True)
    constrol_vars.append(a)
    check = ttk.Checkbutton(check_frame, text="Unchecked", variable=a)
    check.grid(row=index, column=0, padx=5, pady=2, sticky="nsew")
    checkbuttons_skill.append(check)



# Separator
separator = ttk.Separator(root)
separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="Radiobuttons", padding=(20, 10))
radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

# Radiobuttons
radio_1 = ttk.Radiobutton(radio_frame, text="Deselected", variable=d, value=1)
radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
radio_2 = ttk.Radiobutton(radio_frame, text="Selected", variable=d, value=2)
radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(radio_frame, text="Mixed")
radio_3.state(["alternate"])
radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
radio_4 = ttk.Radiobutton(radio_frame, text="Disabled", state="disabled")
radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Label
label = ttk.Label(widgets_frame, text="Full Name")
label.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="w")
# Entry
entry = ttk.Entry(widgets_frame)
entry.insert(0, "")
entry.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")

# Label1
label1 = ttk.Label(widgets_frame, text="Full Name")
label1.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="w")
# Entry2
entry1 = ttk.Entry(widgets_frame)
entry1.insert(0, "")
entry1.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

# Configure column weights for resizing
widgets_frame.columnconfigure(0, weight=0)
widgets_frame.columnconfigure(1, weight=1)
#group all entries in a list
entries = [entry, entry1]
# # Spinbox
# spinbox = ttk.Spinbox(widgets_frame, from_=0, to=100)
# spinbox.insert(0, "Spinbox")
# spinbox.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

# # Combobox
# combobox = ttk.Combobox(widgets_frame, values=combo_list)
# combobox.current(0)
# combobox.grid(row=2, column=1, padx=5, pady=10,  sticky="ew")

# # Read-only combobox
# readonly_combo = ttk.Combobox(widgets_frame, state="readonly", values=readonly_combo_list)
# readonly_combo.current(0)
# readonly_combo.grid(row=3, column=1, padx=5, pady=10,  sticky="ew")

# # Menu for the Menubutton
# menu = tk.Menu(widgets_frame)
# menu.add_command(label="Menu item 1")
# menu.add_command(label="Menu item 2")
# menu.add_separator()
# menu.add_command(label="Menu item 3")
# menu.add_command(label="Menu item 4")

# # Menubutton
# menubutton = ttk.Menubutton(widgets_frame, text="Menubutton", menu=menu, direction="below")
# menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

# # OptionMenu
# optionmenu = ttk.OptionMenu(widgets_frame, e, *option_menu_list)
# optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

# # Button
# button = ttk.Button(widgets_frame, text="Button")
# button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")



# # Togglebutton
# button = ttk.Checkbutton(widgets_frame, text="Togglebutton", style="ToggleButton")
# button.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

# # Switch
# switch = ttk.Checkbutton(widgets_frame, text="Switch", style="Switch")
# switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

# Panedwindow
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
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Treeview columns
treeview.column("#0", anchor="w", width=60)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)

# Treeview headings
treeview.heading("#0", text="Pos", anchor="w")
treeview.heading(1, text="Education", anchor="center")
treeview.heading(2, text="Years of exp", anchor="center")

# Define treeview data
treeview_data = data


# Insert treeview data
for item in treeview_data:
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
    if item[0] == "" or item[2] in (8, 12):
        treeview.item(item[2], open=True) # Open parents

# Select and scroll
treeview.selection_set(1)
treeview.see(4)

# Bind event handler to row click event
treeview.bind("<<TreeviewSelect>>",lambda event: action.handle_row_click(event, treeview, entries))

# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Accentbutton", style="Accent.TButton", 
                          command=lambda:action.delete_data((treeview.index(treeview.selection()))))
accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

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
notebook.add(tab_1, text="Tab 1")

# Scale
scale = ttk.Scale(tab_1, from_=100, to=0, variable=g, command=lambda event: g.set(scale.get()))
scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

# Progressbar
progress = ttk.Progressbar(tab_1, value=0, variable=g, mode="determinate")
progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

# Label
label = ttk.Label(tab_1, text="Forest ttk theme", justify="center")
label.grid(row=1, column=0, pady=10, columnspan=2)

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

# Start the main loop
root.mainloop()
