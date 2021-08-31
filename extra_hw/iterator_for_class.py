class CustomIterator:
    def __init__(self):
        self.current_idx = 0
        self.items = ["name", "age", "gender"]

    def __next__(self):
        if self.current_idx < len(self.items):
            self.current_idx += 1
            key = self.items[self.current_idx-1]
            return key, getattr(self, key)
        else:
            raise StopIteration

    def __iter__(self):
        return self
