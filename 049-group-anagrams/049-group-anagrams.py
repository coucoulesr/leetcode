"""
Leetcode Problem 049: Group Anagrams
Author: Richard Coucoules
"""  

class Solution:
    def groupAnagrams(self, strs):
        set_dict = {}
        for s in strs:
            s_set = frozenset(s)
            if len(s_set) < len(s):
                s_tuple = tuple(sorted(s))
                if s_tuple not in set_dict:
                    set_dict[s_tuple] = [s]
                else:
                    set_dict[s_tuple].append(s)
            else:
                if s_set not in set_dict:
                    set_dict[s_set] = [s]
                else:
                    set_dict[s_set].append(s)
        return [ls for ls in set_dict.values()]

def main():
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs))

if __name__ == "__main__":
    main()