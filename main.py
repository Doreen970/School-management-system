from tkinter import *
from PIL import ImageTk

window = Tk()

window.geometry('1200x800')

background_image = ImageTk.PhotoImage(file='pexels-ylanite-koppens-843227.jpg')

aLabel = Label(window, image=background_image)
aLabel.place(x=0, y=0)

LoginFrame =Frame(window)
LoginFrame.place(x=400, y=200)

lgImage = PhotoImage(file='reading.png')

lgLabel = Label(LoginFrame, image=lgImage)
lgLabel.grid(row=0, column=0, columnspan=2)
usernameImage = PhotoImage(file='user.png')
UsernameLabel = Label(LoginFrame, image=usernameImage, text='Username', compound=LEFT, font=('times new roman', 20, 'bold'))
UsernameLabel.grid(row=1, column=0)
UsernameEntry = Entry(LoginFrame, font=('times new roman', 20, 'bold'))
UsernameEntry.grid(row=1, column=1)

window.mainloop()