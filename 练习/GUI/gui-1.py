from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.inputName = Entry(self)
        self.inputName.pack()
        self.alertButten = Button(self, text='Hello', command=self.hello)
        self.alertButten.pack()
        self.quitButten = Button(self, text='Quit', command=self.quit)
        self.quitButten.pack()

    def hello(self):
        name = self.inputName.get()
        messagebox.showinfo('Message', 'Hello,%s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()



