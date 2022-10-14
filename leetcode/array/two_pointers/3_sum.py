from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        output = []
        global_vis = set()
        nums.sort()
        for i in range(len(nums)-2):
            first_num = nums[i] * -1
            if first_num not in global_vis:
                other_half = set()
                vis = set()
                for j in range(i+1, len(nums)):
                    if first_num - nums[j] in other_half and nums[j] not in vis:
                        output.append([first_num * -1, nums[j], first_num - nums[j]])
                        other_half.remove(first_num - nums[j])
                        vis.add(nums[j])
                    else:
                        other_half.add(nums[j])
                global_vis.add(first_num)
        return output


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([0, 0, 0, 0]))
"""
[-1,0,1,2,-1,-4]
[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
[0,0,0,0]
[0,0,0]
[0,1,1]
[-1,0,1,2,-1,-4,-2,-3,3,0,4]
[0,2,2,3,0,1,2,3,-1,-4,2]
"""