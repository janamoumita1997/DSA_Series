s = "abciiidef"
k = 3

vowels = "aeiou"

def isVowel(letter):
    if letter in vowels:
        return True
    else:
        return False

# def initial_count(s):
#     count = 0
#     for i in range(k):
#         if isVowel(s[i]):
#             count += 1
#     return count

# count = initial_count(s)

# max_count = count
# for i in range(k,len(s)):
#     if isVowel(s[i-k]):
#         count -= 1
#     if isVowel(s[i]):
#         count += 1
#     max_count = max(max_count,count)
    
# print(max_count)


i = 0
count = 0
max_count = 0
while i < len(s):
    if i<k:
        if isVowel(s[i]):
            count += 1
    else:
        if isVowel(s[i]):
            count += 1
        if isVowel(s[i-k]):
            count -= 1
    i += 1
    max_count = max(max_count,count)


print(max_count)   


