class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_len = len(numbers)
        i, j = 0, num_len - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1