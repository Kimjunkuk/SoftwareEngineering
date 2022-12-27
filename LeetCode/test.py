nums =[3,2,4]
target=6

def test():
    n=len(nums)
    # print(n)
    static_value=0
    compare_value=0
    master_value=0
    y=1
    for x in range(n):
        static_value = nums[x]
        # print(x)
        for y in range(n):
            compare_value = nums[y]
            print(y)
            master_value = static_value + compare_value
            # print(master_value, static_value, compare_value)
            if master_value ==  target:
                return [x,y]

test()