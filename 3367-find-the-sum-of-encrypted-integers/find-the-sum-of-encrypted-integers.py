class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            a=str(i)
            maxi=max(a)
            encrypt=int(maxi*len(a))
            ans+=encrypt
        return ans

      

        