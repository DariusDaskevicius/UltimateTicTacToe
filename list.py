from itertools import chain
from typing import List, Union
# shopping basket: "apple": 3, .....
# shopping_basket1 + shopping_basket2 = shopping_basket

class Basket(dict):
    # var1 + var2 => var1.__add__(var2)
    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception(f"Not supported operation for: {other}")

        for item, quantity in other.items():
            if item in self:
                self[item] += quantity
            else:
                self[item] = quantity
        return self

b3 = Basket({"apple": 2, "banana":3})
b4 = Basket({"apple": 4, "avocado":1})
print(b3 + b4)


def merge_baskets(basket1: List[List[Union[str, int]]], basket2: List[List[Union[str, int]]]):
    d = {}
    for (item, quantity) in chain(basket1, basket2):
        if item in d:
            d[item] += quantity
        else:
            d[item] = quantity

    return d



b1 = [["apple", 2], ["banana", 3]]
b2 = [["apple", 4], ["avocado", 1]]

print(merge_baskets(b1, b2))
