
import re

def is_int_str(s):
    return bool(re.match(r'^-?(0|[1-9]\d*)$',s))
def calPoints(ops):
    final_lst = []
    for i in ops:
        if is_int_str(i):
            final_lst.append(int(i))
        elif i == 'C' and len(final_lst)>0:
            final_lst.pop()
        elif i == 'D' and len(final_lst)>0:
            final_lst.append(2*final_lst[-1])
        elif i == '+':
            d = sum(final_lst[-2:])
            final_lst.append(d)
        else:
            final_lst = []
    print(final_lst)
    return sum(final_lst)

ops = ["5","-2","C","C","C","9","+","+"]
print(calPoints(ops))


