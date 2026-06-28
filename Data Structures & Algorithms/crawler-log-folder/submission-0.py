class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stak = 0
        for x in logs :
            if x == '../' and stak == 0 :
                stak = 0
            elif x == '../' and stak != 0 : 
                stak = stak - 1
            elif x == './' :
                stak = stak
            else :
                stak = stak + 1
        return stak
