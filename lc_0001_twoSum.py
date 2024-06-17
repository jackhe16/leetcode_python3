#
# @lc app=leetcode.cn id=1 lang=python3
#


from typing import Dict, List

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable: Dict[int, int] = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []


# @lc code=end
