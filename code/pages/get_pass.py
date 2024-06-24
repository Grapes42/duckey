import tkinter as tk
from tkinter import ttk
import pyperclip

from server import Server
from key_man import Key_man

server = Server("duckey.ddns.net", "duckey", "quack")
key_man = Key_man("keys", "backup_keys")

class GetPass:
    def __init__(self, frame):
        self.frame = frame        

    def construct(self):
        server.get_ids()
        key_man.get_matched(server.ids)

        self.options = key_man.matched_ids

        self.pretty_options = []
        
        for option in self.options:
            split = option.split("-", 1)[1]
            prettied = split.split(".", 1)[0]
            self.pretty_options.append(prettied)
            print(prettied)

        self.searched = [] 
        for option in self.pretty_options:
            self.searched.append(option)
            print(option)
        
        self.list_items = tk.StringVar(value=self.searched)

        #
        # Root content
        #

        self.header = ttk.Label(self.frame, text="Get Password")
        self.prompt = ttk.Label(self.frame, text="Search")

        self.search_input = tk.Text(self.frame, height = 1, width = 30)

        self.listbox = tk.Listbox(
            self.frame,
            height = 8,
            width = 30,
            listvariable=self.list_items
        )

        self.run_search() # runs every 1000ms

        copy_pass = ttk.Button(self.frame, text="Copy Password", command=self.copy_pass)
        copy_user = ttk.Button(self.frame, text="Copy Username")

        
        self.header.grid(row=0, column=0, pady=2, padx=2)
        self.prompt.grid(row=1, column=0, pady=2, padx=2)
        self.search_input.grid(row=2, column=0, pady=2, padx=2)
        self.listbox.grid(row=3, column=0, pady=2, padx=2)

        copy_pass.grid(row=4, column=0, pady=2, padx=2, sticky=tk.W)
        copy_user.grid(row=4, column=0, pady=2, padx=2, sticky=tk.E)
            
    def search(self, field, list):
        txt = field.get(1.0, "end-1c")

        searched = []

        for item in list:
            if txt in item:
                searched.append(item)

        self.list_items.set(searched)

        self.frame.update()
        self.frame.update_idletasks()

    def run_search(self):
        self.search(field=self.search_input, list=self.pretty_options)
        self.frame.after(100, self.run_search)

    def copy_pass(self):
        tuple = self.listbox.curselection()
        index = tuple[0]
        print(self.searched[index])
        pyperclip.copy(self.searched[index])