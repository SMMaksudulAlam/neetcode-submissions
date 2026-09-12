class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_smaller = []
        stack = []
        for i, e in enumerate(heights):
            while(stack and stack[-1][0]>=e):
                stack.pop()
            if(not stack):
                left_smaller.append(-1)
            else:
                left_smaller.append(stack[-1][1])
            stack.append((e, i))
        #print(left_smaller)

        right_smaller = deque([])
        q = deque([])
        for i in range(len(heights)-1, -1, -1):
            e = heights[i]
            while(q and q[0][0]>=e):
                q.popleft()
            if(not q):
                right_smaller.appendleft(len(heights))
            else:
                right_smaller.appendleft(q[0][1])
            q.appendleft((e, i))
        #print(right_smaller)

        ans = 0
        for i in range(len(heights)):
            width = right_smaller[i] - left_smaller[i] - 1
            height = heights[i]
            ans = max(ans, width*height)
        return ans
        
