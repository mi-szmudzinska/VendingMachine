from tkinter import *

#main window
window = Tk()
window.title("Automat z napojami")
window.geometry("500x700")
MainLabel = Label(window, text= "Automat z napojami")
MainLabel.pack()
topFrame = Frame(window)
topFrame.pack()
window.resizable(0,0)
window.configure(background="grey")

#photos
photo1 = PhotoImage(file="water.png")
photo2 = PhotoImage(file="soda.png")
label=Label(window, image=photo1)
label2=Label(window, image=photo2)
label.pack(side=TOP)
label2.pack(side=TOP)

button1=Button(topFrame,text="21: 2.00",fg="blue")
button1.pack(side=LEFT,padx=2,pady=2)

button2=Button(topFrame,text="22: 3.00",fg="blue")
button2.pack(side=LEFT)
#Label(window, image = photo1, bg = "white",).grid(row=1,column=0,sticky=W)
#Label(window, image = photo2, bg = "white",).grid(row=1,column=1,sticky=W)
photo1.put("red")
#run program
window.mainloop()