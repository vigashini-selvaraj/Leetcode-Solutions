class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                res.append(s[i].lower())
           

        ans= "".join(res)
        if ans==ans[::-1]:
            return True
        return False