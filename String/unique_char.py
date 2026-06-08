s = "leetcode"

def firstUniqChar(self, s: str) -> int:
    latter_dict = {}
    for i in range(s):
        latter_dict[i] = latter_dict.get(i,0) + 1
    for i,char in enumerate(s):
        if latter_dict[char] ==1:
            return i
    return -1