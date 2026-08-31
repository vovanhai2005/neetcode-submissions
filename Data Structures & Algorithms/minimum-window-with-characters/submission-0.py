class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        countS = {}
        
        for c in t:
            countT[c] = countT.get(c , 0) + 1
        
        total_cnt = len(countT)
        cur_cnt = 0

        res = [-1 , -1]
        resLen = float("infinity")
        l = 0

        for i in range(len(s)):
            c = s[i]
            countS[c] = countS.get(c , 0) + 1

            if c in countT and countS[c] == countT[c]:
                cur_cnt += 1

            while cur_cnt == total_cnt:
                if (i - l + 1) < resLen:
                    res = [l , i]
                    resLen = i - l + 1
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    cur_cnt -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""




        