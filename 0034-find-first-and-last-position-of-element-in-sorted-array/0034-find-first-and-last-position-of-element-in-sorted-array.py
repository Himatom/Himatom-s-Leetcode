class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(is_first):
            left, right = 0, len(nums) - 1
            pos = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    pos = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                        
            return pos
        
        return [search(True), search(False)]