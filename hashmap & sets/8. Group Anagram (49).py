class Solution:
    def groupAnagrams(self, strs):
         

        # # loop approach to add valuea to dict
        # words = {}
        # for s in strs:
        #     word = ''.join(sorted(s))
        #     if word in words:
        #         words[word].append(s)
        #     else:
        #         words[word] = [s]
        # # return words

        # defaultdict approach
        from collections import defaultdict
        
        words = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            words[key].append(s)

        result = []

        for value in words.values():
            result.append(value)
        return result


x = Solution()
strs = ["eat","tea","tan","ate","nat","bat"] 
print(x.groupAnagrams(strs))