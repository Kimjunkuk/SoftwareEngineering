"""
What is Tuples 
Tuples are data structures that look a lot like lists. Unlike lists, tuples are immutable (meaning that they cannot be modified once created). This restricts their use because we cannot add, remove, or assign values; however, it gives us an advantage in space and time complexities.

A common tuple use is the swapping of  numbers:

a, b = b, a
Here  is a tuple, and it assigns itself the values of .

Another awesome use of tuples is as keys in a dictionary. In other words, tuples are hashable.

튜플(Tuple) vs리스트
-리스트는 []로 둘러싸지만 튜플은 ()으로 둘러싼다.
-리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다. 
>>> t1 = ()
>>> t2 = (1,)  << 한개의 값만 가질때에도 뒤에 콤마(,)를 반드시 붙여야함
>>> t3 = (1, 2, 3)
>>> t4 = 1, 2, 3 << 괄호()를 생략해도 무방함
>>> t5 = ('a', 'b', ('ab', 'cd'))

indexing
>>> t1 = (1, 2, 'a', 'b')
>>> t1[0]
1
>>> t1[3]
'b'

Slicing
>>> t1 = (1, 2, 'a', 'b')
>>> t1[1:]
(2, 'a', 'b')

Combine two tuple
>>> t1 = (1, 2, 'a', 'b')
>>> t2 = (3, 4)
>>> t1 + t2
(1, 2, 'a', 'b', 3, 4)

Multiply tuple
>>> t2 = (3, 4)
>>> t2 * 3
(3, 4, 3, 4, 3, 4)

Length tuple
>>> t1 = (1, 2, 'a', 'b')
>>> len(t1)
4
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
