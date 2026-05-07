def dayOfProgrammer(year):
    # Write your code here
    if 1700 <= year < 1918:
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif 1919 <= year <= 2700:
        if year % 400 == 0 and year % 4 == 0 and year % 100 >0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif year == 1918:
        return "26.09.1918"
    else:
        return f"year {year} beyond the limit"

# print(dayOfProgrammer(1915))

def bonAppetit(bill, k, b):
    # Write your code here
    del bill[k]
    if abs(sum(bill)/2 - b) >0:
        return int(abs(sum(bill)/2 - b))
    else:
        return "Bon Appetit"
bill = [3, 10, 2, 9]
k = 1
b = 7
print(bonAppetit(bill, k, b))