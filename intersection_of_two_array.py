from typing import List
from collections import Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        to_iterate, look_up = self.define_larger_list(nums1, nums2)
        look_up = Counter(look_up)

        for target in to_iterate:
            if target in look_up:
                result.append(target)
                look_up[target] -= 1
                if look_up[target] <= 0:
                    del look_up[target]

        return result
    def define_larger_list(self,l1, l2):
        if l1 > l2:
            return l1, l2
        else:
            return l2, l1



if __name__ == "__main__":
    s = Solution()
    print(s.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
    print(s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))