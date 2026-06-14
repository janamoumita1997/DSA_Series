s = "abab"
p = ""

def is_anagrame(p,s):
    if len(p) != len(s):
        return False
    
    count = {}
    for i in p:
        count[i] = count.get(i,0) + 1

    for j in s:
        count[j] = count.get(j,0) - 1  

    return all(i == 0 for i in count.values())

   
def find_anaIndex(s,p):

    ans = []
    window_size = len(p)
    if window_size == 0:
        return ans
    window = s[:window_size]
    if is_anagrame(p,window):
        ans.append(0)
    for i in range(window_size,len(s)):
        window = window[1:] + s[i]
        if is_anagrame(p,window):
            ans.append(i-window_size+1)
    return ans

print(find_anaIndex(s,p))

