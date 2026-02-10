class SimpleList:
    def __init__(self, items=None):
        self._data = list(items) if items else []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def append(self, value):
        self._data.append(value)

    def __repr__(self):
        return f"SimpleList({self._data!r})"

# Demo:
s = SimpleList([1,2,3])
s.append(4)

print(len(s))      # 4
print(s[2])        # 3
print(3 in s)      # True
for x in s: print(x)