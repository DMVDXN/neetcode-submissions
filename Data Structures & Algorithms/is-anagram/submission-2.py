class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for char in s:
            if char in count_s:
                count_s[char]+=1
            else:
                count_s[char] = 1

        for char in t:
            if char in count_t:
                count_t[char]+=1
            else:
                count_t[char] = 1

        total_s = 0
        total_t = 0

        for count in count_s.values():
            total_s += count

        for count in count_t.values():
            total_t += count

        if count_s != count_t:
            return False
        else:
            return True

        return total_s==total_t 