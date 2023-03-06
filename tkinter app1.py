from tkinter import * 

root = Tk()

root.geometry("400x400")

root.title("My First App ")


button = Label(root,text = "Learning Buttons").pack() 


like = Label(root,
            text = "click to change colour")
like.pack()


def click():
    root.config(bg='blue')

submit = Button(root,
               text = 'click',
               command = click)
submit.pack()

root.mainloop()