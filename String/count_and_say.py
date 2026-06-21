n = 4
# def RLE(n:str) -> str:
#     left = 0
#     seen = n[0]
#     encoded_str = ''
#     for right, val in enumerate(n):
#         if val != seen:
#             encoded_str += f"{right-left}{seen}"
#             seen = val
#             left = right
#     return encoded_str
# print(RLE("3322251"))

from collections import Counter

def RLE(n:str)->str:
    encoded_str = ''
    for k,v in dict(Counter(n)).items():
        encoded_str += f"{v}{k}"
    return encoded_str
# print(RLE("1"))

def count_and_say(n:int)->str:
    if n == 1:
        return "1"
    res = RLE(count_and_say(n-1))
    return res
print(count_and_say(1))

