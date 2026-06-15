
def main(s,k):
    left = 0
    count = {}
    max_freq = 0
    res = 0

    for right, val in enumerate(s):
        count[val] = count.get(val,0) + 1
        max_frq = max(max_freq,count[val])

        windpw_size = right - left + 1
        if windpw_size - max_frq >k:
            count[s[left]] -= 1
            left += 1
        res = max(res,right - left + 1)
    return res
print(main("AABABBA",1))