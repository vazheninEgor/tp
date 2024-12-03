from abc import ABC, abstractmethod

# Интерфейс стратегии
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

# Конкретная стратегия сортировки пузырьком
class BubbleSortStrategy(SortingStrategy):
    def sort(self, array):
        print("Sorting using Bubble Sort")
        # Реализация сортировки пузырьком
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

# Конкретная стратегия быстрой сортировки
class QuickSortStrategy(SortingStrategy):
    def sort(self, array):
        print("Sorting using Quick Sort")
        # Реализация быстрой сортировки
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return self.sort(left) + middle + self.sort(right)

# Контекст, который использует стратегию
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_array(self, array):
        self.strategy.sort(array)

# Пример использования
if __name__ == "__main__":
    sorter = Sorter(BubbleSortStrategy())
    array1 = [5, 3, 8, 4, 2]
    sorter.sort_array(array1)
    print(array1)

    sorter.set_strategy(QuickSortStrategy())
    array2 = [5, 3, 8, 4, 2]
    sorter.sort_array(array2)
    print(array2)