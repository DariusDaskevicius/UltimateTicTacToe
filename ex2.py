x = list(range(9))
print(x)
y = [elem*2 for elem in x]
print(y)
z = [elem for elem in y if elem > 10]
print(z)


map(lambda elem: elem + 100, z)

reduce(lambda first, second: first * second, z)


good_value = "abc"
bad_value = "def"


a = good_value if 5 < 6 else bad_value
print(a)

# class ShoppingBasket:
#     def __init__(self, user):
#         self.user = user
#         self.children = [Node(), Node()]

#     def __repr__(self):
#         return f"ShoppingBasket(user='{self.user}')"

#     def __getitem__(self, name):
#         some_list = []
#         for child in self.children:
#             if child.name == name:
#                 some_list.append(child)

#         if len(some_list) > 1:
#             raise Exception("Too many matches")
#         return list(iter(child))

#     def __add__(self, other):
#         pass


# basket_1 = ShoppingBasket(user="me")
# print(basket_1)

# print(root_node["FlowMonitor"])  # -> root_node 'cleaning' -> child of root node that has the name "FlowMonitor"
# # Node(name="FlowMonitor"....)