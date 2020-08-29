from collections import OrderedDict


class LRUCache:
    def __init__(self, cap):
        # cap:  capacity of cache
        # Intialize all variable
        # code here
        self.cap = cap
        self.ord_dict = OrderedDict()

    # This method works in O(1)
    def get(self, key):
        # code here
        value = self.ord_dict.get(key, -1)
        if value != -1:
            self.ord_dict.move_to_end(key)
        return value

    # This method works in O(1)
    def set(self, key, value):
        # code here
        if key in self.ord_dict:
            self.ord_dict.move_to_end(key)
        else:
            if len(self.ord_dict) == self.cap:
                self.ord_dict.popitem(last=False)
        self.ord_dict[key] = value
