class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = 0

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0]==target:
                return 0
            else:
                return -1
        if nums[0] > nums[right]:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid+1]:
                    pivot = mid+1
                    break
                if nums[mid] < nums[mid-1]:
                    pivot = mid
                    break
                if nums[mid] > nums[0]:
                    left = mid
                if nums[mid] < nums[0]:
                    right = mid   
            if target < nums[0]:
                left = pivot
                right = len(nums)-1
            else:
                left = 0
                right = pivot -1

        while left <= right:
            mid = (left + right) //2
            print(mid)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid -1
            else:
                left = mid +1
        return -1           