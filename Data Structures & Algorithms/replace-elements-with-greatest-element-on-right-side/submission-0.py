class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max, curr = -1, -1
        for i in range(len(arr) - 1, -1, -1):
            curr_max = max(curr_max, arr[i])
            arr[i] = curr
            curr = curr_max
        return arr
