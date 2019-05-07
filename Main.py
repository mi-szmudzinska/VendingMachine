from tkinter import *

#main window
window = Tk()
window.title("Automat z napojami")
window.geometry("500x700")
topFrame = Frame(window)
MainLabel = Label(topFrame, text= "Automat z napojami")
MainLabel.grid()
topFrame.grid(row=0,sticky=N)
window.resizable(0,0)
window.configure(background="white")

#photos
photo1 = PhotoImage(file="water.png")
photo2 = PhotoImage(file="soda.png")
photo3 = PhotoImage(file="juice.png")
photo4 = PhotoImage(file="soda2.png")
photo5 = PhotoImage(file="water.png")
photo6 = PhotoImage(file="soda3.png")
photo7 = PhotoImage(file="juice2.png")
photo8 = PhotoImage(file="beer.png")

label1=Label(window, image=photo1)
label1.grid(row=2,column=0,sticky=NE,padx=10,pady=10)
button1=Button(window,text="21: 2.00",fg="blue")
button1.grid(row=3,column=0,sticky=N,padx=10,pady=0)
#separator=Frame(height=2,bd=1,relief=SUNKEN)
#separator.grid(row=0,column=3,sticky=N, padx=3, pady=3)

label2=Label(window, image=photo2)
label2.grid(row=2,column=1,sticky=N,padx=10,pady=10)
button2=Button(window,text="22: 3.00",fg="blue")
button2.grid(row=3,column=1,sticky=N,padx=10,pady=0)
#separator2=Frame(height=2,bd=1,relief=SUNKEN)
#separator2.grid(row=0,column=3,sticky=NE, padx=3, pady=3)

label3=Label(window, image=photo3)
label3.grid(row=2,column=2,sticky=N,padx=10,pady=10)
button3=Button(window,text="23: 3.00",fg="blue")
button3.grid(row=3,column=2,sticky=N,padx=10,pady=0)

label4=Label(window, image=photo4)
label4.grid(row=2,column=3,sticky=N,padx=10,pady=10)
button4=Button(window,text="24: 5.00",fg="blue")
button4.grid(row=3,column=3,sticky=N,padx=10,pady=0)

label5=Label(window, image=photo5)
label5.grid(row=4,column=0,sticky=NE,padx=10,pady=10)
button5=Button(window,text="25: 2.50",fg="blue")
button5.grid(row=5,column=0,sticky=N,padx=10,pady=0)

label6=Label(window, image=photo6)
label6.grid(row=4,column=1,sticky=N,padx=10,pady=10)
button6=Button(window,text="26: 3.50",fg="blue")
button6.grid(row=5,column=1,sticky=N,padx=10,pady=0)

label7=Label(window, image=photo7)
label7.grid(row=4,column=2,sticky=N,padx=10,pady=10)
button7=Button(window,text="27: 4.00",fg="blue")
button7.grid(row=5,column=2,sticky=N,padx=10,pady=0)

label8=Label(window, image=photo8)
label8.grid(row=4,column=3,sticky=N,padx=10,pady=10)
button8=Button(window,text="25: 5.00",fg="blue")
button8.grid(row=5,column=3,sticky=N,padx=10,pady=0)

#button1=Button(window,text="21: 2.00",fg="blue")
#button1.pack(side=LEFT,padx=2,pady=2)

#button2=Button(window,text="22: 3.00",fg="blue")
#button2.pack(side=LEFT)
#Label(window, image = photo1, bg = "white",).grid(row=1,column=0,sticky=W)
#Label(window, image = photo2, bg = "white",).grid(row=1,column=1,sticky=W)


#run program
window.mainloop()