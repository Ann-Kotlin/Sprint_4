# 129273766
def main(nums: list[int], limit: int) -> int:
    """Основной цикл программы"""
    # Сортировка списка по убыванию
    nums.sort(reverse=True)
    count = 0
    g = len(nums) - 1
    for i in range(len(nums)):
        if i == g:
            count += 1
            return count
        elif i > g:
            return count
        elif nums[i] + nums[g] <= limit:
            count += 1
            g -= 1
        else:
            count += 1
    return count


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    limit = int(input())
    print(main(nums, limit))