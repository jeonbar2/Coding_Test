#백준 1935번
N= int(input())
cal = input()
alpha = [0]*N
stack =[]
for i in range(N):
    alpha[i]=int(input())

for i in cal:
    if 'A'<=i<='Z':
        stack.append(alpha[ord(i) - ord('A')])
    else:
        b=stack.pop()
        a=stack.pop()

        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        elif i =='/':
            stack.append(a/b)

print('%.2f' %stack[0])
