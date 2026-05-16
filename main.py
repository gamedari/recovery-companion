import tkinter as tk
from database import Database

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recovery Companion")
        self.geometry("800x600")
        self.db = Database()
        self.current_user = None
        self.current_frame = None
        self.show_login()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame
        self.current_frame.pack(fill="both", expand=True)

    def show_login(self):
        from screens.login_screen import LoginScreen
        self.show_frame(LoginScreen(self))

    def show_dashboard(self):
        from screens.dashboard_screen import DashboardScreen
        self.show_frame(DashboardScreen(self))

    def show_community(self):
        from screens.community_screen import CommunityScreen
        self.show_frame(CommunityScreen(self))

    def show_leaderboard(self):
        from screens.leaderboard_screen import LeaderboardScreen
        self.show_frame(LeaderboardScreen(self))

    def show_navbar(self):
        navbar = tk.Frame(self, bg="navy", height=50)
        navbar.pack(fill="x", side="top")
        
        tk.Button(navbar, text="Home", command=self.show_dashboard).pack(side="left", padx=10)
        tk.Button(navbar, text="Community", command=self.show_community).pack(side="left", padx=10)
        tk.Button(navbar, text="Leaderboard", command=self.show_leaderboard).pack(side="left", padx=10)
        tk.Button(navbar, text="Logout", command=self.logout).pack(side="right", padx=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()