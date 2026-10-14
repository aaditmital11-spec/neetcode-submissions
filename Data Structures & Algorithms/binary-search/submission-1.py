class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1                 # last index

        while l <= r:
            mid = (l+r)//2            # middle index, recalculated every round

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1              # target is to the right: move which marker?
            else:
                r = mid - 1              # target is to the left: move which marker?

        return -1                # loop ended, range is empty, not found
                    
