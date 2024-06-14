import tkinter as tk
from tkinter import ttk


def search(field, list):
    global listbox

    txt = field.get(1.0, "end-1c")

    searched = []

    for item in list:
        if txt in item:
            searched.append(item)

    list_items = tk.Variable(value=searched)
    
    print(searched)

    listbox = tk.Listbox(
        root,
        height = 10,
        width = 10,
        listvariable=list_items
    )

    root.update()
    root.update_idletasks()

def run_search():
    search(field=search_input, list=options)
    root.after(100, run_search)




root = tk.Tk()
#
# Root attributes
#
root.title("Duckey")

root_width = 500
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

#
# Root content
#

# initial vars
options = ["cat", "mouse", "dog", "bird"]
searched = []
list_items = tk.Variable(value=searched)


header = ttk.Label(root, text="Search")

search_input = tk.Text(root, height = 1, width = 20)


run_search() # runs every 1000ms

header.grid(row = 0, column = 0, pady = 2, padx = 2)
search_input.grid(row = 1, column = 0, pady = 2, padx = 2)
listbox.grid(row = 2, column = 0, pady = 2, padx = 2)

root.mainloop()