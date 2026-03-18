from abc import ABC, abstractmethod


# ─── Strategy Interface ───────────────────────────────────────
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass


# ─── Concrete Strategies ──────────────────────────────────────
class BubbleSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("Sorted using Bubble Sort")
        return arr


class QuickSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left  = [x for x in data if x < pivot]
        mid   = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        print("Sorted using Quick Sort")
        return self.sort(left) + mid + self.sort(right)


class MergeSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        mid   = len(data) // 2
        left  = self.sort(data[:mid])
        right = self.sort(data[mid:])
        print("Sorted using Merge Sort")
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j  = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


# ─── Context ──────────────────────────────────────────────────
class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy          # swap strategy at runtime

    def sort(self, data: list) -> list:
        return self._strategy.sort(data)   # delegates to strategy


# ─── Usage ────────────────────────────────────────────────────
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]

    # Start with bubble sort
    sorter = Sorter(BubbleSortStrategy())
    print(sorter.sort(data))
    # Sorted using Bubble Sort
    # [11, 12, 22, 25, 34, 64, 90]

    # Swap to quick sort at runtime 
    sorter.set_strategy(QuickSortStrategy())
    print(sorter.sort(data))
    # Sorted using Quick Sort
    # [11, 12, 22, 25, 34, 64, 90]

    # Swap to merge sort at runtime
    sorter.set_strategy(MergeSortStrategy())
    print(sorter.sort(data))
    # Sorted using Merge Sort
    # [11, 12, 22, 25, 34, 64, 90]