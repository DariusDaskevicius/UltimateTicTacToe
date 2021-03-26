# from collections.abc import Sequence
from typing import NamedTuple


class Telegram(NamedTuple):
    telegram: str
    reponse: str


class History(list):
    # list[0] = value -> list.__setitem__(0, value)
    def __setitem__(self, index, item):
        raise Exception("Not allowed to modify history objects")

    # var = list[0] -> list.__getitem__(0)
    def __getitem__(self, index):
        return super().__getitem__(index).telegram

    def __iter__(self):
        return (t.telegram for t in super().__iter__())

    def get_telegram_item(self, index):
        return super().__getitem__(index)

    def telegrams(self):
        return super().__iter__()


l = History([Telegram(telegram=f"telegram{i}", reponse=f"reponse{i}") for i in range(4)])
print(l)

simple_list = ["telegram0", "telegram1", "telegram2", "telegram3"]

print(l[0], simple_list[0])

# print(l[0])
# for t in l:
#     print(t)

# print(l.get_telegram_item(1))

for t in l.telegrams():
    print(t)
