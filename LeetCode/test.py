
s = "()[]{}"
stack=[]
closeToOpen={")":"(","]":"[","}":"{"}

# for c in s:
#     if c in closeToOpen:
#         if stack and stack[-1] == closeToOpen[c]:
#             stack.pop()
#         else:
#             print(False)
#     else:
#         stack.append(c)

# print(True) if not stack else False

for c in s:
    # print(c)
    if c in closeToOpen:
        if stack and stack[-1] == closeToOpen[c]:
            stack.pop()
        else:
            print(False) #
    else:
        stack.append(c)