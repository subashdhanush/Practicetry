nums = [1, 2, 3, 5, 6]
n = len(nums) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
print("Missing number:", expected_sum - actual_sum)
