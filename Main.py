from tkinter import *

#main
window = Tk()
window.title("Automat z napojami")
#window(height = 200)
window.resizable(0,0)
window.configure(background = "grey")

#photos
photo1 = PhotoImage(file = "water.png")
photo2 = PhotoImage(file = "soda.png")
Label(window, image = photo1, bg = "white",).grid(row=0,column=0,sticky=W)
Label(window, image = photo2, bg = "white",).grid(row=0,column=0,sticky=W)
#run
window.mainloop()