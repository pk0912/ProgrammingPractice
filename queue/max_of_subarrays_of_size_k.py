from collections import deque
from typing import List


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = 0
        queue = deque()
        output = []
        while end < len(nums):
            while 1:
                if queue:
                    if nums[end] > nums[queue[0]]:
                        queue.popleft()
                    else:
                        break
                else:
                    break
            while 1:
                if queue:
                    popped_index = queue.pop()
                    if nums[popped_index] < nums[end]:
                        continue
                    else:
                        queue.append(popped_index)
                        queue.append(end)
                        break
                else:
                    queue.append(end)
                    break
            if end == start + k - 1:
                start += 1
                end += 1
                output.append(nums[queue[0]])
                while 1:
                    if not (start <= queue[0] < start + k - 1):
                        queue.popleft()
                    else:
                        break
            else:
                end += 1
        return output


sol = Solution()
print(sol.maxSlidingWindow([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
