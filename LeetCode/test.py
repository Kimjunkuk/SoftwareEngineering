arry=[1,0,2,3,0,4,5,0]
zerocounter=0
n=0
for x in range(len(arry)):
    if arry[n] == 0: 
        arry.insert(n, 0) 
        n+=1
        zerocounter+=1
    n+=1
arry=arry[:-zerocounter]

print(arry)

# arry.insert(1, 0)
# print(arry[:-2])
# # print(arry)