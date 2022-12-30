numRows=5
k=1
temp=[]
for x in range(numRows):
    line=[]
    for y in range(k):
        line.append(1)
    k+=1
    temp.append(line)
p=1
for i in range(numRows):
    n=len(temp[i])
    for j in range(p):
        if i > 1 and j >= 1 and j < n-1:
            l=temp[i-1][j-1]
            r=temp[i-1][j]
            temp[i][j]=l+r
    p+=1
print(temp)