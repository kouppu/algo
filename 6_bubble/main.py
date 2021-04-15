import random
from typing import List


def buble_sort(numbers: List[int]) -> List[int]:
    numbers_len = len(numbers)
    for i in range(len(numbers)):
        for j in range(numbers_len - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(10)]
    print(nums)
    print(buble_sort(nums))
