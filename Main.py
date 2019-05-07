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
photo2 = PhotoImage(file="water.png")
photo3 = PhotoImage(file="juice.png")
photo4 = PhotoImage(file="juice.png")
photo5 = PhotoImage(file="soda.png")
photo6 = PhotoImage(file="soda.png")
photo7 = PhotoImage(file="juice2.png")
photo8 = PhotoImage(file="juice2.png")
photo9 = PhotoImage(file="beer.png")
photo10 = PhotoImage(file="beer.png")
photo11 = PhotoImage(file="soda3.png")
photo12 = PhotoImage(file="soda3.png")
photo13 = PhotoImage(file="soda2.png")
photo14 = PhotoImage(file="soda2.png")
photo15 = PhotoImage(file="milk.png")
photo16 = PhotoImage(file="milk.png")

label1=Label(window, image=photo1)
label1.grid(row=2,column=0,sticky=NE,padx=10,pady=10)
button1=Button(window,text="30: 2.00",fg="blue")
button1.grid(row=3,column=0,sticky=NE,padx=18,pady=0)
#separator=Frame(height=2,bd=1,relief=SUNKEN)
#separator.grid(row=0,column=3,sticky=N, padx=3, pady=3)

label2=Label(window, image=photo2)
label2.grid(row=2,column=1,sticky=N,padx=10,pady=10)
button2=Button(window,text="31: 3.00",fg="blue")
button2.grid(row=3,column=1,sticky=N,padx=10,pady=0)
#separator2=Frame(height=2,bd=1,relief=SUNKEN)
#separator2.grid(row=0,column=3,sticky=NE, padx=3, pady=3)

label3=Label(window, image=photo3)
label3.grid(row=2,column=2,sticky=N,padx=10,pady=10)
button3=Button(window,text="32: 3.00",fg="blue")
button3.grid(row=3,column=2,sticky=N,padx=10,pady=0)

label4=Label(window, image=photo4)
label4.grid(row=2,column=3,sticky=N,padx=10,pady=10)
button4=Button(window,text="33: 5.00",fg="blue")
button4.grid(row=3,column=3,sticky=N,padx=10,pady=0)

label5=Label(window, image=photo5)
label5.grid(row=4,column=0,sticky=NE,padx=10,pady=10)
button5=Button(window,text="34: 2.50",fg="blue")
button5.grid(row=5,column=0,sticky=NE,padx=18,pady=0)

label6=Label(window, image=photo6)
label6.grid(row=4,column=1,sticky=N,padx=10,pady=10)
button6=Button(window,text="35: 3.50",fg="blue")
button6.grid(row=5,column=1,sticky=N,padx=10,pady=0)

label7=Label(window, image=photo7)
label7.grid(row=4,column=2,sticky=N,padx=10,pady=10)
button7=Button(window,text="36: 4.00",fg="blue")
button7.grid(row=5,column=2,sticky=N,padx=10,pady=0)

label8=Label(window, image=photo8)
label8.grid(row=4,column=3,sticky=N,padx=10,pady=10)
button8=Button(window,text="37: 5.00",fg="blue")
button8.grid(row=5,column=3,sticky=N,padx=10,pady=0)

label9=Label(window, image=photo9)
label9.grid(row=6,column=0,sticky=NE,padx=10,pady=10)
button9=Button(window,text="38: 2.00",fg="blue")
button9.grid(row=7,column=0,sticky=NE,padx=18,pady=0)

label10=Label(window, image=photo10)
label10.grid(row=6,column=1,sticky=N,padx=10,pady=10)
button10=Button(window,text="39: 3.00",fg="blue")
button10.grid(row=7,column=1,sticky=N,padx=10,pady=0)

label11=Label(window, image=photo11)
label11.grid(row=6,column=2,sticky=N,padx=10,pady=10)
button11=Button(window,text="40: 3.00",fg="blue")
button11.grid(row=7,column=2,sticky=N,padx=10,pady=0)

label12=Label(window, image=photo12)
label12.grid(row=6,column=3,sticky=N,padx=10,pady=10)
button12=Button(window,text="41: 5.00",fg="blue")
button12.grid(row=7,column=3,sticky=N,padx=10,pady=0)

label13=Label(window, image=photo13)
label13.grid(row=8,column=0,sticky=NE,padx=10,pady=10)
button13=Button(window,text="42: 2.50",fg="blue")
button13.grid(row=9,column=0,sticky=NE,padx=18,pady=0)

label14=Label(window, image=photo14)
label14.grid(row=8,column=1,sticky=N,padx=10,pady=10)
button14=Button(window,text="43: 3.50",fg="blue")
button14.grid(row=9,column=1,sticky=N,padx=10,pady=0)

label15=Label(window, image=photo15)
label15.grid(row=8,column=2,sticky=N,padx=10,pady=10)
button15=Button(window,text="44: 4.00",fg="blue")
button15.grid(row=9,column=2,sticky=N,padx=10,pady=0)

label16=Label(window, image=photo16)
label16.grid(row=8,column=3,sticky=N,padx=10,pady=10)
button16=Button(window,text="45: 5.00",fg="blue")
button16.grid(row=9,column=3,sticky=N,padx=10,pady=0)

#button1=Button(window,text="21: 2.00",fg="blue")
#button1.pack(side=LEFT,padx=2,pady=2)

#button2=Button(window,text="22: 3.00",fg="blue")
#button2.pack(side=LEFT)
#Label(window, image = photo1, bg = "white",).grid(row=1,column=0,sticky=W)
#Label(window, image = photo2, bg = "white",).grid(row=1,column=1,sticky=W)


#run program
window.mainloop()