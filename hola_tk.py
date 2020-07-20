import tkinter as tk

class mywindow:
    def __init__(self, root):
        root.geometry("200x100")
        button = tk.Button(app,text="Ok", command=self.hola)
        button.pack()

    def hola(self):
        print("ahoy")

app = tk.Tk()
window = mywindow(app)

app.mainloop()


