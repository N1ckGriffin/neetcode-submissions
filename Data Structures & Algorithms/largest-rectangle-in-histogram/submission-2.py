class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        

        for i, h in enumerate(heights):
            prevIndex = i
            while stack and stack[-1][0] > h:
                prevHeight, prevIndex = stack.pop()
                maxArea = max(maxArea, (i - prevIndex) * prevHeight)

            stack.append((h, prevIndex))

        while stack:
            prevHeight, prevIndex = stack.pop()
            maxArea = max(maxArea, (len(heights) - prevIndex) * prevHeight)

        return maxArea


        