# community_screen.py (Em's file)
import tkinter as tk

class CommunityScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="Community Screen - Em's work goes here").pack()