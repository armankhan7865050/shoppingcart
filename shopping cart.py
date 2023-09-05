class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product_name):
        for item in self.items:
            if item['product'].name == product_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total

    def display_cart(self):
        for item in self.items:
            print(f"{item['product'].name} - ${item['product'].price} x {item['quantity']}")
        print(f"Total: ${self.calculate_total()}")

if __name__ == "__main__":
    apple = Product("Apple", 0.5)
    banana = Product("Banana", 0.25)
    orange = Product("Orange", 0.75)

    cart = ShoppingCart()
    cart.add_item(apple, 5)
    cart.add_item(banana, 3)
    cart.add_item(orange, 2)

    cart.display_cart()

    cart.remove_item("Banana")

    print("\nAfter removing Banana:")
    cart.display_cart()
