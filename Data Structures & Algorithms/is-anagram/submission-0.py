class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        
        tab={}

        for a in s:
            tab[a]= tab.get(a,0)+1
        
        for b in t:
            if b not in tab or tab[b]==0:
                return False
                
            else:
                tab[b]-=1
        
        
        return True
