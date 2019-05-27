from tkinter import *


class MachineException(Exception):

    def __init__(self, msg):
        self.msg = msg


class IncorrectProductNumberException(MachineException):
    def __init__(self):
        super().__init__("Niepoprawny numer produktu!")


class NotEnoughMoneyException(MachineException):
    def __init__(self, price):
        super().__init__("Niewystarczająca ilość pieniędzy!\nCena produktu: " + str(price/100) + " zł.")


class OnlyExactMoneyException(MachineException):
    def __init__(self):
        super().__init__("Tylko odliczona kwota!.")


class ProductUnavailableException(MachineException):
    def __init__(self):
        super().__init__('Produkt niedostępny.')


class WithdrawException(MachineException):
    def __init__(self):
        super().__init__('Nie wrzuciłeś żadnych monet.')


class Item:
    def __init__(self, name):
        self.name = name


class Product(Item):
    def __init__(self, name, price):
        super(Product, self).__init__(name)
        self.price = price
        self.quanity = 5


class Machine:
    coin_types = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    coins = None

    products = {}
    choosen = None

    def __init__(self):
        super().__init__()

        self.init_products()

        self.init_coins_dicts()

        self.get_inserted()

    def init_coins_dicts(self):
        self.coins = {}
        for c in self.coin_types:
            self.coins[c] = {
                'owned': 1,
                'inserted': 0
            }

    def get_inserted(self):
        return {key: self.coins[key]['inserted'] for key, value in self.coins.items() if
                self.coins[key]['inserted'] > 0}

    def get_inserted_value(self):
        v = 0
        for key, value in self.coins.items():
            v += key * value['inserted']
        return v

    def get_coin_ammount(self, dict):
        counter = 0
        for key, value in dict.items():
            counter += value
        return counter

    def connect_coin_dict(self, dict1, dict2):
        result = dict1.copy()
        for key in dict2:
            if key in result:
                result[key] += dict2[key]
            else:
                result[key] = dict2[key]
        return result

    def check_available_coins(self, dict):
        for key, value in dict.items():
            available = self.coins[key]['owned'] + self.coins[key]['inserted']
            if value > available:
                return False
        return True

    def payment(self, product_number):
        if product_number not in self.products:
            raise IncorrectProductNumberException

        product = self.products[product_number]
        if product.quanity < 1:
            raise ProductUnavailableException
        price = product.price
        inserted = self.get_inserted_value()
        change = inserted - price
        if change < 0:
            raise NotEnoughMoneyException(self.products[product_number].price)
        elif change == 0:
            product.quanity -= 1
            self.clear_inserted()
            return 'Brak reszty.', product

        temp_dict = {}
        for key, value in self.coins.items():
            temp_dict[key] = value['owned']
            temp_dict[key] += value['inserted']

        past_dict = {
            0: {}
        }
        for i in range(1, change + 1):
            for coin in self.coin_types:
                rest = i - coin
                if rest < 0:
                    continue

                if rest not in past_dict:
                    continue

                dict = {coin: 1}
                new_dict = self.connect_coin_dict(
                    past_dict[rest],
                    dict
                )

                if not self.check_available_coins(new_dict):
                    continue
                if i not in past_dict:
                    past_dict[i] = new_dict
                else:
                    if self.get_coin_ammount(past_dict[i]) > self.get_coin_ammount(new_dict):
                        past_dict[i] = new_dict

        if change not in past_dict:
            raise OnlyExactMoneyException

        for key in self.coins:
            self.coins[key]['owned'] += self.coins[key]['inserted']
        for key in past_dict[change]:
            self.coins[key]['owned'] -= past_dict[change][key]

        self.clear_inserted()

        product.quanity -= 1

        return past_dict[change], product

    def get_product_price(self, product_number):
        if product_number not in self.products:
            raise IncorrectProductNumberException
        return self.products[product_number].price

    def withdraw(self):
        if self.get_inserted_value() == 0:
            raise WithdrawException
        result = self.get_inserted().copy()
        self.clear_inserted()
        return result

    def clear_inserted(self):
        for key in self.coins:
            self.coins[key]['inserted'] = 0

    def insert_coin(self, v):
        self.coins[v]['inserted'] += 1

    def init_products(self):
        self.products[30] = Product("Woda 0.3l", 150)
        self.products[31] = Product("Woda 0.5l", 200)
        self.products[32] = Product("Coca-Cola 0.33l", 250)
        self.products[33] = Product("Coca-Cola 0.5l", 500)
        self.products[34] = Product("Sprite 0.33l", 250)
        self.products[35] = Product("Sprite 0.5l", 500)
        self.products[36] = Product("Fanta 0.33l", 250)
        self.products[37] = Product("Fanta 0.5l", 500)
        self.products[38] = Product("Ice tea 0.33l", 50)
        self.products[39] = Product("Ice tea 0.5l", 450)
        self.products[40] = Product("Tiger 0.20l", 350)
        self.products[41] = Product("RedBull 0.20l", 890)
        self.products[42] = Product("Fanta 0,33l", 150)
        self.products[43] = Product("Fanta 0,5l", 400)
        self.products[44] = Product("Tonic 0.33l", 320)
        self.products[45] = Product("Tonic 0.5l", 470)
        self.products[46] = Product("Monster 0,5l", 500)
        self.products[47] = Product("Woda gaz 0,2l", 130)
        self.products[48] = Product("Woda gaz 0,33l", 200)
        self.products[49] = Product("Woda gaz 0,5l", 260)
