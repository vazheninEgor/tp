# Интерфейс итератора
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

# Конкретный итератор
class ArrayIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0
    
    def has_next(self):
        return self.position < len(self.items)
    
    def next(self):
        if self.has_next():
            item = self.items[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration("No more items")

# Пример использования
if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]
    iterator = ArrayIterator(items)
    
    while iterator.has_next():
        print(iterator.next())