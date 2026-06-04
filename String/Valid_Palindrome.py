s = "A man, a plan, a canal: Panama"

import re
def find_palindrome(s):
    s = s.lower().strip()
    res1 = re.sub(r'[^a-zA-Z0-9]','',s)
    res2 = res1[::-1]
    if res1 == res2:
        return True
    else:
        return False
    
print(find_palindrome(s))