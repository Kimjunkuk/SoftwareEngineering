"""
1st
def count_substring(string, sub_string):
    num=0
    print("len_substring:"+str(len(sub_string)))
    for x in range(len(string)):
      y=int(len(sub_string))
      print("x:"+str(x))
      print("y"+str(y))
      if sub_string != string[x:y]:
        print("range"+str(x)+":"+str(y)+":"+string[x:y])
        y+=1
      else:
        num+=1
    print(num)
    return num

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)
    
    #1
    #2
    #3
    #4
    #5
    #6
    #7
    #8
    #9
    #10
    #11
    #12
    
"""


def count_substring(string, sub_string): #1
    num=0 #2
    y=int(len(sub_string)) #3
    z=0 #4
    for x in range(len(string)): #4
      if str(sub_string) != str(string[int(z):int(y)]): #5
        print("range"+str(z)+":"+str(y)+":"+string[int(z):int(y)]) #6
        print("sub_string"+sub_string) #7
        print("string"+string) #8
        z=z+1 #9
        y=y+1 #10
      elif str(sub_string) != str(string[int(z):int(y)]): #11
        num+=1 #12
    return num #13

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)
