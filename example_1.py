


# def wrapper(func):
#     def inter(*args):
#         return_vals = None
#         for i in range(3):
#             try:
#                 return_vals = func(*converted_args)
#             except Exception:
#                 continue

#         return return_vals

#     return inter

# @wrapper
# def test(a, b):
#     print(a, b)

# @wrapper
# def test2(a, b, c):
#     print(a, b, c)

# test(1, 2)
# test2(1, 2, 3)


class Converters:
    @staticmethod
    def format_output():
        return ""

    @classmethod
    def to_json(cls):
        return cls.format_output()

    @classmethod
    def to_xml(cls):
        return cls.format_output()


class Car:
    doors = 4

    def __init__(self, model):
        self.model = model

    @classmethod
    def print_parameters(cls):
        print(cls.doors)
        cls.print_hello()


    @classmethod
    def print_hello(cls):
        print("hello")


c1 = Car("honda")
c2 = Car("vw")

print(c1.model, c1.doors)
print(c2.model, c2.doors)

Car.doors = 7

print(c1.model, c1.doors)
print(c2.model, c2.doors)

c1.print_parameters()
Car.print_parameters()
c2.print_parameters()


# --------------------
from typing import Dict
from requests import request

def fetch_data(url) -> Dict:
    r = requests.request(url)
    r.get()
    if r.code != 200:
        print("error")

    return r.data.decode("utf-8")

# --------------------

# class One:
#     @staticmethod
#     def one():
#         print("abc")

#     @classmethod
#     def two(cls):
#         print(cls.__name__)


# One.one()
# One.two()

# getter/setters -> python