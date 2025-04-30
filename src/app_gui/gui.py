import tkinter as tk
import webbrowser


class AppGui():
    def __init__(self, root):
        self.root = root
        self.root.title("Event Creator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

    def create_button(self, program_flow):    
        self.button = tk.Button(self.root, text="🎤︎︎", width=100, height=50, font=("Arial", 16), borderwidth = 0, command=program_flow)
        self.button.pack(padx=60, pady=60)

    def create_label(self, text, program_flow):
        for widget in self.root.winfo_children():
            widget.destroy()
        w = tk.Label(self.root, text=text, font=("Arial", 12), wraplength=250)
        w.pack(side=tk.TOP, pady=10)
        # Add the button back
        self.create_button(program_flow)

    def create_link_label(self, parent, text, url, program_flow):
        for widget in self.root.winfo_children():
            widget.destroy()
        link_label = tk.Label(parent, text=text, cursor="hand2", font=("Arial", 12), wraplength=250)
        link_label.bind("<Button-1>", lambda e: webbrowser.open_new(url))
        link_label.pack(side=tk.TOP, pady=1)
        # Add the button back
        self.create_button(program_flow)
