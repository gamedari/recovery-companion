# dashboard_screen.py (T's file)
import tkinter as tk

class DashboardScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="Dashboard Screen - T's work goes here").pack()