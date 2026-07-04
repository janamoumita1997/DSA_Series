def generateParentheses(n:int)->list:
    res = []
    def backtrack_parentheses(current_string,open_count,close_count):
        if len(current_string) == 2*n:
            res.append(current_string)
            return
        
        if open_count < n:
            backtrack_parentheses(current_string +'(',open_count+1,close_count)
        if close_count<open_count:
            backtrack_parentheses(current_string + ')',open_count,close_count+1)
        
    backtrack_parentheses('',0,0)
    return res

print(generateParentheses(3))