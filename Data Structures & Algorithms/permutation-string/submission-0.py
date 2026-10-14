class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        need = {}
        window = {}

        for c in s1:
            need[c] = 1 + need.get(c, 0)

        left = 0
        for right in range(len(s2)):
            c = s2[right]
            window[c] = 1 + window.get(c, 0)

            if right - left + 1 > len(s1):
                old = s2[left]
                window[old] -= 1 

                if window[old] == 0:
                    del window[old]

                left += 1

            if need == window:
                return True
        
        return False