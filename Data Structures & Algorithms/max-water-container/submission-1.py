class Solution:
    def area(self, heights, i, j):
        return min(heights[i], heights[j]) * (j - i)

    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        max_area = 0
        while i < j:
            curr_area = self.area(heights, i, j)
            max_area = max(curr_area, max_area)
            # print(i, j, max_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area
