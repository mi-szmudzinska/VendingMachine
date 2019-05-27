# VendingMachine
Vending Machine project in Python
with Tkinter library.
## Task description:
* The machine stores information about coins in it (1, 2, 5, 10, 20, 50gr, 1, 2, 5 PLN)
* The machine stores information about the goods in it (items with numbers from 30 to 50), each included in the price (by default, 5 pieces of each item)
* Dialog box with buttons for sending coins, a field for displaying coins, buttons for data transmission, buttons 0-9 allowing obtaining the item number.

Selected after selecting the correct item number:
* If a coin is thrown, a window informing about the price in the machine pops up.
* If you are interested in a value greater than or equal to the price of the product, the machine is available and can spend the rest
* Lack of commodity: a window pops up with information about the lack in the machine.
* Lack of data / can be issued: a window pops up with information about the purchase, issues the rest (rejected coins, rejected as the rest, counted down the data).
* Can not spend: a window pops up saying "Only the amount deducted".

## Tests:
1. Checking the price of one item - expected price information.
2. Putting the deducted amount, purchase of goods - expected lack of rest.
3. Including a larger amount, purchase of goods - expected rest.
4. Purchase of the entire assortment, purchase attempt after the goods have been used up - expected information about the lack.
5. Checking the price of goods with an incorrect number (50) - expected error information.
6. Putting in a few coins, stopping the transaction - expected return of coins.
7. Throwing in a small amount, choosing the correct item number, throwing the rest of the coins to the deducted amount, re-selecting the correct item number - expected no rest.
8. Purchase of goods by paying 1 gr - the sum of one hundred coins is to be equal to PLN 1 (for floats the sum of 100 times 0.01 + 0.01 + ... + 0.01 will not be equal to 1.0). Payments can be made using the for loop in the interpreter.

## Technologies:
* Python
