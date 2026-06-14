s = "ababaa"
p = "ab"
ns, np = len(s), len(p)


# Frequency arrays for 26 letters
freqP = [0] * 26
freqS = [0] * 26

# Build frequency for pattern p
for char in p:
    freqP[ord(char) - ord('a')] += 1

# First window in s
for i in range(np):
    freqS[ord(s[i]) - ord('a')] += 1

result = []
if freqS == freqP:
    result.append(0)

# Slide the window
for i in range(np, ns):
    freqS[ord(s[i]) - ord('a')] += 1
    freqS[ord(s[i - np]) - ord('a')] -= 1
    if freqS == freqP:
        result.append(i - np + 1)


