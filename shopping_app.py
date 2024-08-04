from customer import Customer
from item import Item
from seller import Seller


seller = Seller("DIC")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memory", 13880, seller)
    Item("Motherboard", 28980, seller)
    Item("Power Unit", 8980, seller)
    Item("PC Case", 8727, seller)
    Item("3.5-inch HDD", 10980, seller)
    Item("2.5-inch SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU Cooler", 13400, seller)
    Item("Graphics Card", 23800, seller)

print("🤖 Please tell me your name")
customer = Customer(input())

print("🏧 Enter the amount to charge into your wallet")
customer.wallet.deposit(int(input()))

print("🛍️ Shopping is starting")
end_shopping = False
while not end_shopping:
    print("📜 Product List")
    seller.show_items()

    print("️️⛏ Please enter the product number")
    number = int(input())

    print("⛏ Please enter the quantity")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Cart Contents")
    customer.cart.show_items()
    print(f"🤑 Total Amount: {customer.cart.total_amount()}")

    print("😭 Do you want to end shopping? (yes/no)")
    end_shopping = input() == "yes"

print("💸 Do you want to confirm the purchase? (yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Result┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ {customer.name}'s possessions")
customer.show_items()
print(f"😱👛 {customer.name}'s wallet balance: {customer.wallet.balance}")

print(f"📦 {seller.name}'s inventory")
seller.show_items()
print(f"😻👛 {seller.name}'s wallet balance: {seller.wallet.balance}")

print("🛒 Cart Contents")
customer.cart.show_items()
print(f"🌚 Total Amount: {customer.cart.total_amount()}")

print("🎉 End")