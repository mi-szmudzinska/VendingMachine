from tkinter import messagebox
from functools import partial
from machine import *


class BorderFrame(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.configure(borderwidth=2, relief="ridge")


class CoinUI(BorderFrame):
    def __init__(self, machine):
        super().__init__()

        self.machine = machine
        self.chosen_product = None
        self.coins_value = StringVar()
        self.coins_value.set("0.0")
        self.product_number = StringVar()
        self.product_number.set("")
        self.initUI()

    def add(self, v):
        self.machine.insert_coin(v)
        self.update_entries()

    def update_entries(self):
        print(self.machine.get_inserted_value())
        coin_value = self.machine.get_inserted_value()
        self.coins_value.set(float("{0:.2f}".format(coin_value / 100)))

    def initUI(self):
        self.master.title("Review")
        self.pack(fill=BOTH, expand=True)

        counter = 0
        frame = BorderFrame(self)
        frame.pack()
        for key, value in self.machine.coins.items():
            if counter % 3 == 0:
                f = Frame(frame)
                f.pack()
            part = partial(self.add, key)
            if float(key) < 100:
                text = str(int(key)) + " gr"
            else:
                text = str(int(key / 100)) + " zł"

            button = Button(f, command=part, text=text, width=6)
            button.pack(side=LEFT, padx=5, pady=5)
            counter += 1

        f = BorderFrame(self)
        f.pack()
        frame = Frame(f)
        frame.pack()
        label = Label(frame, text="Kredyty")
        label.pack(side=LEFT, padx=5, pady=5)
        entry = Entry(frame, textvariable=self.coins_value, state='readonly', justify='right', width=12)
        entry.pack(padx=5, pady=5)

        frame = Frame(f)
        frame.pack()
        label = Label(frame, text="Numer")
        label.pack(side=LEFT, padx=5, pady=5)
        entry = Entry(frame, textvariable=self.product_number, state='readonly', justify='right', width=12)
        entry.pack(padx=5, pady=5)

        frame = BorderFrame(self)
        frame.pack()
        for i in range(1, 11):
            if i % 3 == 1:
                f = Frame(frame)
                f.pack()
            if i == 10:
                part = partial(self.keyboard_click, -2)
                button = Button(f, command=part, text='Clear', width=6)
                button.pack(side=LEFT, padx=5, pady=5)
            part = partial(self.keyboard_click, i % 10)
            button = Button(f, command=part, text=i % 10, width=6)
            button.pack(side=LEFT, padx=5, pady=5)
            if i == 10:
                part = partial(self.keyboard_click, -1)
                button = Button(f, command=part, text='<', width=6)
                button.pack(side=LEFT, padx=5, pady=5)

        f = BorderFrame(self)
        f.pack()
        frame = Frame(f)
        frame.pack()
        button = Button(frame, command=self.withdraw, text="Wypłać", width=6)
        button.pack(side=LEFT, padx=5, pady=5)
        button = Button(frame, command=self.pay, text="Zapłać", width=6)
        button.pack(side=LEFT, padx=5, pady=5)

    def keyboard_click(self, v):
        if v == -1:
            number = self.product_number.get()
            if len(number) > 1:
                number = int(number)
                number /= 10
                self.product_number.set(int(number))
            else:
                self.product_number.set('')
        elif v == -2:
            self.product_number.set("")
        elif v == -9:
            print(self.machine.coins)
        else:
            number = self.product_number.get()
            if len(number) > 0:
                number = int(number)
                number *= 10
                v += number
            self.product_number.set(v)

    def pay(self):
        if self.product_number.get() is '':
            return
        else:
            try:
                value, product = self.machine.payment(int(self.product_number.get()))
                info_1 = "Zakupiono produkt:\n\n\t" + product.name + '\n\n'
                if type(value) is str:
                    messagebox.showinfo('OK', info_1 + value)
                else:
                    info_2 = "Reszta:"
                    for k, v in value.items():
                        if k < 100:
                            t = str(int(k)) + ' gr'
                        else:
                            t = str(int(k / 100)) + ' zł'
                        info_2 += "\n\t" + str(int(v)) + ' x ' + t
                    messagebox.showinfo('OK', info_1 + info_2)

                self.product_number.set('')
                self.update_entries()
            except MachineException as e:
                messagebox.showinfo('Error', e.msg)

    def withdraw(self):
        try:
            value = self.machine.withdraw()
            info_1 = "Wypłaciłacasz:"
            for k in value:
                if k < 100:
                    t = str(int(k)) + ' gr'
                else:
                    t = str(int(k / 100)) + ' zł'
                info_1 += "\n\t" + str(int(value[k])) + ' x ' + t
            messagebox.showinfo('OK', info_1)
            self.product_number.set('')
            self.update_entries()
        except MachineException as e:
            messagebox.showinfo('Warning', e.msg)

    def set_choosen(self, product):
        if product is not None:
            self.chosen_product = product
        else:
            self.chosen_product = None

        self.update_entries()


class ProductsUI(BorderFrame):
    def __init__(self, machine, coin_ui):
        super().__init__()

        self.machine = machine
        self.coin_ui = coin_ui
        self.coins_value = StringVar()
        self.coins_value.set("0.0")

        self.choosed = None

        self.initUI()

    def choose(self, product, button):
        if self.choosed is not None:
            self.choosed.configure(relief=RAISED)
            if self.choosed is button:
                self.choosed = None
                self.coin_ui.set_choosen(None)
                return

        self.choosed = button
        button.configure(relief=SUNKEN)

        self.coin_ui.set_choosen(product)

    def initUI(self):
        self.master.title("Vending Maschine")
        self.pack(fill=BOTH, expand=True)

        counter = 0
        f = None
        for id, product in self.machine.products.items():
            if counter % 4 == 0:
                f = Frame(self)
                f.pack()

            product_frame = Frame(f, borderwidth=2, relief="ridge")
            Label(product_frame, text=str(id), width=11).pack(padx=5, pady=2)
            Label(product_frame, text=str(product.name)).pack(padx=5, pady=2)
            Label(product_frame, text="Cena: " + str("{0:.2f}".format(product.price / 100))).pack(padx=5, pady=2)

            product_frame.pack(side=LEFT, padx=5, pady=5)
            counter += 1


class Program(Frame):

    def __init__(self):
        super().__init__()

        self.machine = Machine()
        self.initUI()

    def initUI(self):
        self.master.title("Coin machine")

        coin_ui = CoinUI(self.machine)
        product_ui = ProductsUI(self.machine, coin_ui)

        product_ui.pack(side=LEFT)
        coin_ui.pack(side=RIGHT)


def main():
    root = Tk()
    Program()
    root.geometry("700x450+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
