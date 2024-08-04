class Cart:
    from item_manager import show_items
    from ownable import set_owner

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Insufficient balance. Checkout failed.")
        else:
            for item in self.items:
                item.owner.wallet.balance += item.price  # Transfer the money to item owner
                self.owner.wallet.balance -= item.price
                item.owner = self.owner  # Transfer ownership to cart owner
            self.items = []  # Empty the cart