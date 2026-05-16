# login_screen.py (L's file)
import tkinter as tk

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="Login Screen - L's work goes here").pack()