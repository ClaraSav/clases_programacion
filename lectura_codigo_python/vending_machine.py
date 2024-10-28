class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def reduce_stock(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False

class VendingMachine:
    def __init__(self):
        self.inventory = {
            'A1': Product('Water', 1.00, 10),
            'A2': Product('Soda', 1.50, 5),
            'A3': Product('Cookies', 2.00, 3),
            'A4': Product('Chocolate', 1.75, 7),
        }
        self.inserted_money = 0.0

    def show_products(self):
        for code, product in self.inventory.items():
            print(f'{code}: {product.name} - ${product.price} ({product.quantity} in stock)')

    def insert_money(self, amount):
        self.inserted_money += amount
        print(f'Inserted money: ${amount:.2f}')

    def select_product(self, code):
        if code not in self.inventory:
            print('Product not available')
            return
        
        product = self.inventory[code]
        if product.quantity == 0:
            print('Product out of stock')
            return
        
        if self.inserted_money < product.price:
            print('Insufficient funds')
            return
        
        if product.reduce_stock(1):
            self.inserted_money -= product.price
            print(f'{product.name} dispensed. Remaining balance: ${self.inserted_money:.2f}')
        else:
            print('Error dispensing product')

    def return_change(self):
        change = self.inserted_money
        self.inserted_money = 0
        print(f'Change returned: ${change:.2f}')

if __name__ == "__main__":
    machine = VendingMachine()
    
    money = float(input('Enter moner: '))

    machine.insert_money(money)
    machine.select_product('A2')
    machine.select_product('A3')
    machine.return_change()
