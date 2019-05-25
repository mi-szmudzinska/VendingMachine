import unittest
from machine import *


class TestMachine(unittest.TestCase):

    def setUp(self):
        self.machine = Machine()

    def test_get_product_price(self):
        self.assertEqual(250, self.machine.get_product_price(32))

    def test_no_change(self):
        self.machine.insert_coin(200)
        self.machine.insert_coin(50)

        result = self.machine.payment(32)
        self.assertEqual('Brak reszty.', result[0])

    def test_get_change(self):
        self.machine.coins[10]['owned'] = 1

        self.machine.insert_coin(200)
        self.machine.insert_coin(20)
        self.machine.insert_coin(20)
        self.machine.insert_coin(20)

        result = self.machine.payment(32)
        self.assertEqual({10: 1}, result[0])

    def test_out_of_stock(self):
        self.machine.insert_coin(200)
        self.machine.insert_coin(50)
        self.machine.payment(32)
        self.machine.insert_coin(200)
        self.machine.insert_coin(50)
        self.machine.payment(32)
        self.machine.insert_coin(200)
        self.machine.insert_coin(50)
        self.machine.payment(32)
        self.machine.insert_coin(200)
        self.machine.insert_coin(50)
        self.machine.payment(32)
        self.machine.insert_coin(200)
        self.machine.insert_coin(50)
        self.machine.payment(32)
        self.machine.insert_coin(200)
        self.machine.insert_coin(50)

        self.assertRaises(ProductUnavailableException, self.machine.payment, 32)

    def test_get_non_existing_product_price(self):
        self.assertRaises(IncorrectProductNumberException, self.machine.get_product_price, 3)

    def test_withdraw_money(self):
        self.machine.insert_coin(200)
        self.machine.insert_coin(50)
        self.machine.insert_coin(10)
        self.machine.insert_coin(50)
        self.assertEqual({10: 1, 50: 2, 200: 1}, self.machine.withdraw())

    def test_add_more_coins(self):
        self.machine.insert_coin(100)
        self.machine.insert_coin(50)
        self.assertRaises(NotEnoughMoneyException, self.machine.payment, 32)

        self.machine.insert_coin(100)
        result = self.machine.payment(32)
        self.assertEqual('Brak reszty.', result[0])

    def test_pay_in_cents(self):
        for i in range(250):
            self.machine.insert_coin(1)
        result = self.machine.payment(32)
        self.assertEqual('Brak reszty.', result[0])
