import tkinter as tk
from tkinter import ttk

from encryption import Encryption
enc = Encryption(host="duckey.ddns.net", username="duckey", password="quack")

class AddPass:
    def __init__(self, frame):
        self.frame = frame        

    def construct(self):
        #
        # Root content
        #

        self.header = ttk.Label(self.frame, text="Add Password")
        
        # Prompts
        self.passname_prompt = ttk.Label(self.frame, text="Password Name")
        self.username_prompt = ttk.Label(self.frame, text="Username")
        self.password_prompt = ttk.Label(self.frame, text="Password")

        # Input fields
        self.passname_input = tk.Text(self.frame, height=1, width=20)
        self.username_input = tk.Text(self.frame, height=1, width=20)
        self.password_input = tk.Text(self.frame, height=1, width=20)

        # Buttons
        self.add_pass_button = ttk.Button(self.frame, text="Add Password", command=self.gui_add_pass, width=16)

        # Grid
        self.header.grid(row=0, column=0, pady=2, padx=2, columnspan=2)

        self.passname_prompt.grid(row=1, column=0, pady=2, padx=2)
        self.passname_input.grid(row=1, column=1, pady=2, padx=2)

        self.username_prompt.grid(row=2, column=0, pady=2, padx=2)
        self.username_input.grid(row=2, column=1, pady=2, padx=2)

        self.password_prompt.grid(row=3, column=0, pady=2, padx=2)
        self.password_input.grid(row=3, column=1, pady=2, padx=2)

        self.add_pass_button.grid(row=4, column=1)

    def gui_add_pass(self):
        passname = self.passname_input.get(1.0, "end-1c")
        username = self.username_input.get(1.0, "end-1c")
        password = self.password_input.get(1.0, "end-1c")

        enc.encrypt_and_store(passname=passname, username=username, password=password)

        