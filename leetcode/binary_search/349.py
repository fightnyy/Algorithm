class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        result = set()
        for v in nums2:
            idx = bisect.bisect_left(nums1, v)
            print(idx)
            if len(nums1) > idx and nums1[idx] == v:
                result.add(v)
        return result


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(nums2)
