from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello World!')
        self.helloLabel.pack()
        self.quitButten = Button(self, text='Quit', command=self.quit)
        self.quitButten.pack()


app = Application()
app.master.title('Hello World')
app.mainloop()



