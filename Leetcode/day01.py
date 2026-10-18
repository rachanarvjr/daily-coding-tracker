# Platform: LeetCode
# Problem: Running Sum of 1d Array
# Language: Python

nums = [1, 2, 3, 4, 5]
result = []
total = 0

for num in nums:
    total += num
    result.append(total)

print(result)
