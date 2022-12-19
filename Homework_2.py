class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"It is a {self.__class__}, which show you products of our shop. " \
               f"You hold {self.name} which costs {self.price}."

    def __float__(self):
        return self.price

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def get_total(self, quantity):
        return round(self.price * quantity, 2)


class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.quantities = []

    def __repr__(self) -> str:
        return f"It is a {self.__class__}, which contains all products, that you want to buy."

    def __float__(self):
        return self.total_price()

    def __add__(self, other):
        another_cart = ShoppingCart()
        another_cart.products, another_cart.quantities = self.products.copy(), self.quantities.copy()
        if isinstance(other, Product):
            another_cart.add_product(other, 1)
        elif isinstance(other, ShoppingCart):
            for product, quantity in zip(other.products, other.quantities):
                another_cart.add_product(product, quantity)
        return another_cart

    def add_product(self, product: Product, quantity) -> None:
        if product in self.products:
            position = self.products.index(product)
            self.quantities[position] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total_price(self):
        total = 0
        for (product, quantity) in zip(self.products, self.quantities):
            total += product.get_total(quantity)
        return total


if __name__ == "__main__":
    product1 = Product("beer", 38)
    product2 = Product("milk", 44.5)
    product3 = Product('bar', 19.99)
    product4 = Product('sausage', 30)
    product5 = Product('pasta', 36)

    product6 = Product('tomato', 7.7)
    product7 = Product('tomato', 7.7)

    cart1 = ShoppingCart()
    cart1.add_product(product1, 8)
    cart1.add_product(product2, 1)
    cart1.add_product(product3, 2)
    cart1.add_product(product4, 0)
    cart1.add_product(product5, 3)
    cart1.add_product(product6, 7)
    cart1.add_product(product1, 8)

    cart2 = ShoppingCart()
    cart2.add_product(product1, 8)
    cart2.add_product(product2, 1)
    cart2.add_product(product3, 2)

    assert cart1.total_price() == 854.38
    assert product1.get_total(8) == 304
    assert product7 == product6

    print(product1.__repr__())
    print(cart1)
    print(f'CART 1: {cart1}'
          f'Total price for all products = {cart1.total_price()} UAH')
    print(f'CART 2: {cart2} '
          f'Total price for all products = {cart2.total_price()} UAH')

