class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        stack = []
        left_boundaries = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_boundaries[i] = stack[-1]
            stack.append(i)
        left_boundaries = [l + 1 for l in left_boundaries]

        stack = []
        right_boundaries = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_boundaries[i] = stack[-1]
            stack.append(i)
        right_boundaries = [r - 1 for r in right_boundaries]

        max_area = 0
        for i in range(n):
            curr_area = heights[i] * (right_boundaries[i] - left_boundaries[i] + 1)
            max_area = max(max_area, curr_area)

        return max_area
