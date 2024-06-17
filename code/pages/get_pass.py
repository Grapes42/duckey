import tkinter as tk
from tkinter import ttk
import pyperclip

class GetPass:
    def __init__(self, options):
        #
        # Root attributes
        #

        self.root = tk.Tk()
        self.root.title("Duckey - Get Pass")

        root_width = 500
        root_height = 300

        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Find the center point
        center_x = int(screen_width/2 - root_width / 2)
        center_y = int(screen_height/2 - root_height / 2)


        self.root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)
        self.root.attributes('-topmost', 1)
        
        #
        # Initial options
        #
        self.options = options
        self.searched = options

        self.list_items = tk.StringVar(value=self.searched)

        #
        # Root content
        #

        self.header = ttk.Label(self.root, text="Search")

        self.search_input = tk.Text(self.root, height = 1, width = 30)

        self.listbox = tk.Listbox(
            self.root,
            height = 10,
            width = 30,
            listvariable=self.list_items
        )

        self.run_search() # runs every 1000ms

        copy_pass = ttk.Button(self.root, text="Copy Password", command=self.copy_pass)
        copy_user = ttk.Button(self.root, text="Copy Username")

        self.header.grid(row=0, column=0, pady=2, padx=2)
        self.search_input.grid(row=1, column=0, pady=2, padx=2)
        self.listbox.grid(row=2, column=0, pady=2, padx=2)

        copy_pass.grid(row=3, column=0, pady=2, padx=2, sticky=tk.W)
        copy_user.grid(row=3, column=0, pady=2, padx=2, sticky=tk.E)
            
    def search(self, field, list):
        txt = field.get(1.0, "end-1c")

        searched = []

        for item in list:
            if txt in item:
                searched.append(item)

        self.list_items.set(searched)

        self.root.update()
        self.root.update_idletasks()

    def run_search(self):
        self.search(field=self.search_input, list=self.options)
        self.root.after(100, self.run_search)

    def copy_pass(self):
        tuple = self.listbox.curselection()
        index = tuple[0]
        print(self.searched[index])
        pyperclip.copy(self.searched[index])

    def run(self):
        self.root.mainloop()