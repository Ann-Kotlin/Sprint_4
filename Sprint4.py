# 129887867
def quantity(nums: list[int], limit: int) -> int:
    """Основной цикл программы"""
    # Сортировка списка по убыванию
    nums_sored = sorted(nums, reverse=True)
    count = 0
    right = len(nums) - 1
    left = 0
    while left <= right:
        if nums_sored[right] + nums_sored[left] <= limit:
            right -= 1
            left += 1
        else:
            left += 1
        count += 1           
    return count


if __name__ == '__main__':
    nums = [int(number) for number in input().split()]
    limit = int(input())
    print(quantity(nums, limit))