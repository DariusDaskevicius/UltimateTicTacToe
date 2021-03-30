from typing import Dict


# Library
# Can't change logic INSIDE of merge & add
# --------------------------`-----------------------
class History:
    def merge(self, history1: Dict, history2: Dict):
        pass

    def add(self, history1: Dict, history2: Dict):
        pass
# --------------------------------------------------

h = History()


# -----
# can;t revert/change this
def get_info():
    # return {}, {}  -> old implementation
    # new implementation
    return Data(data={}, index=1), Data(data={}, index=2)
# -----


# business logic
# -----------------------
# can't change this
data1, data2 = get_info()

h.merge(data1, data2)
h.add(data1, data2)
# ------------------------


class Data:
    def __init__(self, data, index):
        self.data = data
        self.index = index
