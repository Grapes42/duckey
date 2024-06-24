import tkinter as tk
from tkinter import ttk

from pages.get_pass import GetPass
from pages.add_pass import AddPass

def clear():
    for widget in app_frame.winfo_children():
        widget.destroy()

def get_pass_switch():
    clear()
    get_pass.construct()

def add_pass_switch():
    clear()
    add_pass.construct()





#
# Root attributes
# 
root = tk.Tk()
root.title("Duckey - Password Manager")

root_width = 450
root_height = 300

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - root_width / 2)
center_y = int(screen_height/2 - root_height / 2)

root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-topmost', 1)

# Main app frame
app_frame = tk.Frame(root)
change_frame = tk.Frame(root)

app_frame.grid(row=0, column=0)
change_frame.grid(row=0, column=1, sticky=tk.NSEW)


get_pass_change = ttk.Button(change_frame, text="Get Password", command=get_pass_switch, width=16)
add_pass_change = ttk.Button(change_frame, text="Add Password", command=add_pass_switch, width=16)

get_pass_change.grid(row=0)
add_pass_change.grid(row=1)


# Defining window objects
get_pass = GetPass(frame=app_frame)
add_pass = AddPass(frame=app_frame)


root.grid_columnconfigure(0, weight=1)

get_pass.construct()

root.mainloop()