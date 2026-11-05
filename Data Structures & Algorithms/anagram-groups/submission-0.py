class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        

        for word in strs:

            length = len(word)
            
            freq={}
            
            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] =1

            key= tuple(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key]=[word]

        return list(groups.values()) 
