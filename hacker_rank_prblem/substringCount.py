

s = "aba"
n = 10

#output len s contain a and concatenate the s to s
m = ""
cnt = 0
flag = 0

for j in range(1,n):
    for i in s:
        m += i
        if i == 'a':
            cnt += 1
        if len(m) == n:
            flag = 1
            break
    if flag == 1:
        break
    

print(m)
print(cnt)
    
        
    
    