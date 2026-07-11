class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen=set()
        left=0
        curr=0
        ans=0
        for right in range(len(nums)):
            while nums[right] in seen :
                seen.remove(nums[left])
                curr-=nums[left]
                left+=1
            seen.add(nums[right])
            curr += nums[right]
            ans = max(ans, curr)
        return ans

       

        