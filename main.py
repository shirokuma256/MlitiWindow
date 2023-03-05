import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=True)

        # Create the list of app windows
        self.app_windows = []

        # Create the frame for the app windows
        self.app_frame = tk.Frame(self, bg='white')
        self.app_frame.pack(side='top', fill='both', expand=True)

        # Bind the drag-and-drop events to the app frame
        self.app_frame.bind("<ButtonPress-1>", self.start_move)
        self.app_frame.bind("<B1-Motion>", self.on_move)

        # Create the button for adding apps
        add_button = tk.Button(self, text='Add App', command=self.add_app)
        add_button.pack(side='bottom')

        # Bind the resize event to the main window
        self.master.bind('<Configure>', self.on_resize)

    def add_app(self):
        # Create a new app window
        app_window = tk.Toplevel(self)
        app_window.geometry('400x300')
        app_window.title('App Window')

        # Add the app window to the list and display it
        self.app_windows.append(app_window)
        app_window.lift()

    def on_resize(self, event):
        # Resize the app windows to match the size of the app frame
        for app_window in self.app_windows:
            app_window.geometry('%dx%d' % (self.app_frame.winfo_width(), self.app_frame.winfo_height()))

    def start_move(self, event):
        # Save the position of the mouse when the drag starts
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def on_move(self, event):
        # Calculate the new position of the app frame based on the mouse position
        delta_x = event.x - self._drag_start_x
        delta_y = event.y - self._drag_start_y
        x = self.app_frame.winfo_x() + delta_x
        y = self.app_frame.winfo_y() + delta_y

        # Move the app frame to the new position
        self.app_frame.place(x=x, y=y)

# Create the main window and run the application
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    root.title('App Launcher')
    app = MainApplication(root)
    app.mainloop()