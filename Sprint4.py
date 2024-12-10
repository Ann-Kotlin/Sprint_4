# 129566869
def quantity(nums: list[int], limit: int) -> int:
    """Основной цикл программы"""
    # Сортировка списка по убыванию
    nums_sored = sorted(nums, reverse=True)
    count = 0
    left = len(nums) - 1
    for right in range(len(nums)):
        if right == left:
            break
        elif right > left:
            return count
        elif nums_sored[right] + nums_sored[left] <= limit:
            left -= 1
        count += 1    
    count += 1        
    return count


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    limit = int(input())
    print(quantity(nums, limit))