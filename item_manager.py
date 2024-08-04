from item import Item
from tabulate import tabulate
from itertools import groupby


def items_list(
    self,
):  # Returns all Item instances owned by the entity itself (where the entity is the owner).
    items = [item for item in Item.item_all() if item.owner == self]
    return items


def pick_items(
    self, number, quantity
):  # Returns the Item instances owned by the entity corresponding to the given number and quantity.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]


def show_items(
    self,
):  # Outputs the inventory status of Item instances owned by the entity in tabular form with columns ["Number", "Product Name", "Price", "Quantity"].
    table_data = []
    for stock in _stock(self):
        table_data.append(
            [
                stock["number"],
                stock["label"]["name"],
                stock["label"]["price"],
                len(stock["items"]),
            ]
        )
    print(
        tabulate(
            table_data,
            headers=["Number", "Product Name", "Price", "Quantity"],
            tablefmt="grid",
        )
    )  # Uses the tabulate module to output the results in a table format.


def _stock(
    self,
):  # Returns the inventory status of Item instances owned by the entity itself.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(
        item_ls, key=lambda m: m.name
    ):  # Classifies Item instances with the same value returned by Item#name.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append(
            {
                "number": index,
                "label": {"name": item[0].name, "price": item[0].price},
                "items": item,
            }
        )  # The items list contains classified Item instances.
    return stock