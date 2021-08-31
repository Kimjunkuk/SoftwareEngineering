
""""
x,y,z, n 에 대한 값은 주어준다. 
x,y,z에 대한 중복되지 않는 모든 경우의 수를 구하는 문제이다.
x,y,z의 값 중 가장 큰 수의 값을 넘을 수 없다. 
리스트의 기능을 사용할 필요 없음 출력만 예시와 같이 하면됨

x,y,z를모든 경우의 수 출력
 
[x,y,z]

그리고 x,y,z의 합이 n이 되는 경우는 출력하지 않음 
if x+y+z!=n:

반복출력 첫번째는 0,0,0으로 출력하여서 0,0,1 으로 마지막 수가 z의 수 까지 1씩 증가
x 반복 i부터 x까지 출력 하는데(조건) y가 출력된 후 값증가 
y 반복 k부터 y까지 출력 하는데(조건) z가 출력된 후 값증가
z 반복 u부터 z까지 출력 print for z in range(z)"""
"""
Concept

You have already used lists in previous hacks. List comprehensions are an elegant way to build a list without having to use different for loops to append values one by one. These examples might help.

The simplest form of a list comprehension is:

[ expression-involving-loop-variable for loop-variable in sequence ]

This will step over every element in a sequence, successively setting the loop-variable equal to every element one at a time. It will then build up a list by evaluating the expression-involving-loop-variable for each one. This eliminates the need to use lambda forms and generally produces a much more readable code than using map() and a more compact code than using a for loop.

>> ListOfNumbers = [ x for x in range(10) ] # List of integers from 0 to 9
>> ListOfNumbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
List comprehensions can be nested where they take the following form:

[ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]

This is equivalent to writing:

results = []
for outer_loop_variable in outer_sequence:
    for inner_loop_variable in inner_sequence:
        results.append( expression_involving_loop_variables )
For example, if you want to generate all combinations of lists  and , write:

>>> print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
[[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]
This is equivalent to:

>>> results = []
>>> for x in [1, 2, 3]:
...     for y in [4, 5, 6]:
...         results.append([x, y])
... 
>>> print(results)
[[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]

The final form of list comprehension involves creating a list and filtering it similar to using the filter() method. The filtering form of list comprehension takes the following form:

[ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]

This form is similar to the simple form of list comprehension, but it evaluates boolean-expression-involving-loop-variable for every item. It also only keeps those members for which the boolean expression is True.

>> ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
>> ListOfThreeMultiples
[0, 3, 6, 9]"""

"""

https://docs.python.org/3/tutorial/datastructures.html

>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
"""
