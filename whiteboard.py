import tkinter as tk

class WhiteboardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Whiteboard App")
        
        
        self.canvas = tk.Canvas(self.master, bg="white", width=600, height=400)
        self.canvas.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)
        
        
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        
        
        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        self.clear_button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        
        
        self.color_buttons_frame = tk.Frame(self.master)
        self.color_buttons_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N)

        colors = ["black", "red", "green", "blue" , "yellow"]  
        for i, color in enumerate(colors):
            color_button = tk.Button(self.color_buttons_frame, bg=color, width=2, command=lambda c=color: self.set_color(c))
            color_button.grid(row=i, column=0, padx=2, pady=2, sticky=tk.W)

        self.current_color = "black"
        self.start_x = None
        self.start_y = None

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        
    def draw(self, event):
        if self.start_x and self.start_y:
            x1, y1 = self.start_x, self.start_y
            x2, y2 = event.x, event.y
            self.canvas.create_line(x1, y1, x2, y2, fill=self.current_color, width=2)
            self.start_x, self.start_y = x2, y2
        
    def clear_canvas(self):
        self.canvas.delete("all")

    def set_color(self, color):
        self.current_color = color

def main():
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
