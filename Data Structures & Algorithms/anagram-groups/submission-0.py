from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict is a subclass of dict `{}`
        res = defaultdict(list)


        # iter through strs
        for string in strs:
            k = self.generate_key(string)
            res[k].append(string)



        return list(res.values())

    def generate_key(self, string: str):
        '''
        ret key that indexes into res
        '''
        
        counts = [0] * 26
        
        for s in string:
            counts[ord(s) - ord("a")] += 1
        
        return ",".join(str(c) for c in counts)