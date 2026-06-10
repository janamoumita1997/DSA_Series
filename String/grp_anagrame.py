strs = ["eat","tea","tan","ate","nat","bat"]

grp_dict = {}
for i in strs:
    key = ''.join(sorted(i))
    if key not in grp_dict:
        grp_dict[key] = []
    grp_dict[key].append(i)
ans = list(grp_dict.values())
print(ans)





