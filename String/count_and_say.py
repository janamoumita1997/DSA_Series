n = 4
def RLE(n:str) -> str:
    count = 1
    encoded_str = ''
   
    for i in range(1,len(n)):
        if n[i] == n[i-1]:
            count += 1

        else:
            encoded_str += str(count)+n[i-1]
            count = 1
            
    encoded_str += str(count) + n[-1]
    return encoded_str






def count_and_say(n:int)->str:
    if n == 1:
        return "1"
    res = RLE(count_and_say(n-1))
    return res
print(count_and_say(5))

