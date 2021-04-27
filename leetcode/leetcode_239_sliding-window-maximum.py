class Solution:
    def maxSlidingWindow(self, nums, k):
        d = deque()
        answer = deque()
        for i in range(len(nums)):
            if d and i - d[0] >= k:
                d.popleft()

            while d and nums[i] >= nums[d[-1]]:
                d.pop()
            d.append(i)

            if i >= k - 1:
                answer.append(nums[d[0]])

        return answer
