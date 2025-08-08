from typing import List

def can_partition_k_groups(nums: List[int], k: int) -> bool:
    target = sum(nums) // k
    used = [False] * len(nums)
    
    def dfs(start, k, current_sum):
        if k == 0:
            return True
        if current_sum == target:
            return dfs(0, k - 1, 0)
        for i in range(start, len(nums)):
            if not used[i] and current_sum + nums[i] <= target:
                used[i] = True
                if dfs(i + 1, k, current_sum + nums[i]):
                    return True
                used[i] = False
        return False

    return sum(nums) % k == 0 and dfs(0, k, 0)

def max_equal_sum_groups(arr: List[int]) -> int:
    total = sum(arr)
    arr.sort(reverse=True)  # helps in pruning
    for k in range(len(arr), 0, -1):
        if total % k == 0:
            if can_partition_k_groups(arr, k):
                return k
    return 1  # fallback if no partition possible

# Examples
print(max_equal_sum_groups([3,3,3,3]))         # Output: 4
print(max_equal_sum_groups([1, 2, 3, 4, 5, 6])) # Output: 3
print(max_equal_sum_groups([1, 2, 3, 8]))       # Output: 1
# print(max_equal_sum_groups([5, 11, 1, 5])) 