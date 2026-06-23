s = "PAYPALISHIRING"
numRows = 4

row = [''] * numRows

current_row = 0
go_down = False


for i in s:
    row[current_row] += i

    if current_row == 0 or current_row == numRows - 1:
        go_down = not go_down
    
    current_row += 1 if go_down else -1

res = ''.join(row)
print(res)
