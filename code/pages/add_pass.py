import tkinter as tk
from tkinter import ttk

class AddPass:
    def __init__(self, frame, key_man_object, server_object):
        self.frame = frame        

        self.key_man = key_man_object
        self.server = server_object
    def construct(self):
        #
        # Root content
        #

        self.header = ttk.Label(self.frame, text="Add Password")
        
        # Prompts
        self.name_prompt = ttk.Label(self.frame, text="Password Name")
        self.pass_prompt = ttk.Label(self.frame, text="Password")

        # Input fields
        self.name_input = tk.Text(self.frame, height=1, width=20)
        self.pass_input = tk.Text(self.frame, height=1, width=20)

        # Buttons
        self.add_pass_button = ttk.Button(self.frame, text="Add Password", command=self.gui_add_pass, width=16)

        # Grid
        self.header.grid(row=0, column=0, pady=2, padx=2, columnspan=2)

        self.name_prompt.grid(row=1, column=0, pady=2, padx=2)
        self.name_input.grid(row=1, column=1, pady=2, padx=2)

        self.pass_prompt.grid(row=2, column=0, pady=2, padx=2)
        self.pass_input.grid(row=2, column=1, pady=2, padx=2)

        self.add_pass_button.grid(row=3, column=1)

    def gui_add_pass(self):
        pass_name = self.name_input.get(1.0, "end-1c")
        password = self.pass_input.get(1.0, "end-1c")

        print(pass_name)
        print(password)

        self.key_man.get_keys()

        self.server.add_pass(id=self.key_man.id, 
                        public_key=self.key_man.public_key,
                        pass_name=pass_name,
                        password=password)

        