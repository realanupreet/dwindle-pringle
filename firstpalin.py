class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def chkpalin(word):
            s=0
            e=len(word)-1
            while s<e:
                if word[s]!=word[e]:
                    return False
                s+=1
                e-=1
            return True
        for w in words:
            if chkpalin(w):
                return w
        return ""