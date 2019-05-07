from tkinter import *

#main window
window = Tk()
window.title("Automat z napojami")
window.geometry("500x700")
topFrame = Frame(window)
MainLabel = Label(topFrame, text= "Automat z napojami")
MainLabel.grid(row=0,column=0,sticky=N)

topFrame.grid()
window.resizable(0,0)
window.configure(background="grey")

#photos
photo1 = PhotoImage(file="water.png")
photo2 = PhotoImage(file="soda.png")
photo3 = PhotoImage(file="juice.png")
photo4 = PhotoImage(file="soda2.png")
photo5 = PhotoImage(file="water.png")
photo6 = PhotoImage(file="soda3.png")
photo7 = PhotoImage(file="juice2.png")
photo8 = PhotoImage(file="beer.png")

label=Label(window, image=photo1,padx=100,pady=100)
label.grid(row=2,column=0,sticky=E)

label2=Label(window, image=photo2,padx=2,pady=2)
label2.grid(row=2,column=1,sticky=E)

label3=Label(window, image=photo3,padx=2,pady=2)
label3.grid(row=2,column=3,sticky=E)

label4=Label(window, image=photo4,padx=2,pady=2)
label4.grid(row=2,column=4,sticky=E)

label5=Label(window, image=photo5,padx=2,pady=2)
label5.grid(row=3,column=0,sticky=E)

label6=Label(window, image=photo6,padx=2,pady=2)
label6.grid(row=3,column=1,sticky=E)

label7=Label(window, image=photo7,padx=2,pady=2)
label7.grid(row=3,column=3,sticky=E)

label8=Label(window, image=photo8,padx=2,pady=2)
label8.grid(row=3,column=4,sticky=E)

button1=Button(window,text="21: 2.00",fg="blue")
#button1.pack(side=LEFT,padx=2,pady=2)

button2=Button(window,text="22: 3.00",fg="blue")
#button2.pack(side=LEFT)
#Label(window, image = photo1, bg = "white",).grid(row=1,column=0,sticky=W)
#Label(window, image = photo2, bg = "white",).grid(row=1,column=1,sticky=W)
photo1.put("red")
#run program
window.mainloop()