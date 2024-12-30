from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title = title
        self.canvas = Canvas()
        self.canvas.pack()
        self.window_is_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.window_is_running = True
        
        while self.window_is_running is True:
            self.redraw()

    def close(self):
        self.window_is_running = False
