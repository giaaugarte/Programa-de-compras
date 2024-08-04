from user import User
from cart import Cart


class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)