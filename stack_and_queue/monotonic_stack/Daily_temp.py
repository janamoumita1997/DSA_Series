temperatures = [73,74,75,71,69,72,76,73]

stack = []

n = len(temperatures)
output = [0] * n
for i in range(n-1,-1,-1):

    while stack and stack[-1][0] <= temperatures[i]:
            stack.pop()

    if stack and stack[-1][0] > temperatures[i]:
        output[i] = stack[-1][1] - i

    stack.append((temperatures[i],i))

print(output)