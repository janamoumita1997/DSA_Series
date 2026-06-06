s = "  "

def isVowel(char):
    vowels = ['a','e','i','o','u']
    if char.lower() in vowels:
        return True
    else:
        return False
    
# print(isVowel("b"))

s = list(s)
n = len(s)
i,j = 0,n-1
while i<j:
    if isVowel(s[i]) and isVowel(s[j]):
        temp = s[j]
        s[j] = s[i]
        s[i] = temp
        i += 1
        j -= 1
    elif isVowel(s[i]) and not isVowel(s[j]):
        j -= 1
    elif not isVowel(s[i]) and isVowel(s[j]):
        i += 1
    else:
        i += 1
        j -= 1
ans = ''.join(s)
print(ans)
