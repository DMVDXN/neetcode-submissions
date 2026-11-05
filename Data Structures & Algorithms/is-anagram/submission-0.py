class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        visited= {}
        visited_t= {}

        for char in s:
            if char in visited:
                visited[char]+=1
            else:
                visited[char]=1

        for char in t:
            if char in visited_t:
                visited_t[char]+=1
            else:
                visited_t[char]=1

        return visited==visited_t