import math
from collections import deque

def main():
    _list()
    _list_stack()
    _list_queue()
    _list_comprehensions()
    _list_nested_comprehensions()
    _del()
    _tuples()
    _set()
    _dictionary()
    _loop()
    _cond()
    _other()

def _list():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print(fruits)
    print(fruits.count('apple'))
    print(fruits.count('guava'))
    print(fruits.index('banana'))
    print(fruits.index('banana', 4))
    fruits.reverse()
    print(fruits)
    fruits.sort()
    print(fruits)
    print(fruits.pop())
    print(fruits)

def _list_stack():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)
    print(stack.pop())
    print(stack)

def _list_queue():
    queue = deque([3, 4, 5])
    queue.append(6)
    queue.append(7)
    print(queue)
    print(queue.popleft())
    print(queue)

def _list_comprehensions():
    squares = []
    for i in range(10):
        squares.append(i**2)
    print(squares)
    squares2 = list(map(lambda x: x**2, range(10)))
    print(squares2)
    squares3 = [x**2 for x in range(10)]
    print(squares3)

    comps = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(comps)
    comps2 = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                comps2.append((x, y))
    print(comps2)

    vec = [-4, -2, 0, 2, 4]
    vec1 = [x*2 for x in vec]
    print(vec1)

    vec2 = [x for x in vec if x > 0]
    print(vec2)

    vec3 = [abs(x) for x in vec]
    print(vec3)

    fruits = [' orange ', ' apple ', ' pear ', ' banana ']
    print(fruits)
    fruits2 = [x.strip() for x in fruits]
    print(fruits2)

    seq_list = [(x, x**2) for x in range(5)]
    print(seq_list)

    two_way_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(two_way_list)
    one_way_list = [num for row in two_way_list for num in row]
    print(one_way_list)

def _list_nested_comprehensions():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print(matrix)

    matrix2 = [[row[i] for row in matrix] for i in range(4)]
    print(matrix2)

    matrix3 = []
    for i in range(4):
        matrix3.append([row[i] for row in matrix])
    print(matrix3)

    matrix4 = []
    for i in range(4):
        matrix4_row = []
        for row in matrix:
            matrix4_row.append(row[i])
        matrix4.append(matrix4_row)
    print(matrix4)

    matrix5_tuple = list(zip(*matrix))
    print(matrix5_tuple)

    matrix6_list = list(map(list, zip(*matrix)))
    print(matrix6_list)

def _del():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list)

    del list[0]
    print(list)

    del list[2:4]
    print(list)

    del list[:]
    print(list)

def _tuples():
    t = 1, 2, 'hi'
    print(t[0])
    print(t)

    u = t, (1, 2, 3), 1, 2, 3
    print(u)
    # u[0] = 1 tuple immutable
    v = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
    print(v)
    # v[0] = [0, 0, 0] immutable

    empty_tuple = ()
    print(empty_tuple)

    one_tuple = (1,)
    print(one_tuple)

    x, y, z = t
    print(z)

def _set():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    print('apple' in basket)
    print('kiwi' in basket)

    a = set('abracadabra')
    b = set('alacazam')

    print(f'a:{a}')
    print(f'b:{b}')
    print(f'a - b: {a - b}')
    print(f'a | b: {a | b}')
    print(f'a & b: {a & b}')
    print(f'a ^ b: {a ^ b}')

def _dictionary():
    tel = {'Allen': 912, 'Jack': 910}
    tel['Austin'] = 988
    print(tel)
    print(tel['Jack'])

    del tel['Austin']
    print(tel)

    tel['David'] = 932
    print(tel)

    print(list(tel))
    print(sorted(tel))

    print('Jack' in tel)
    print('Jack' not in tel)

    dict1 = dict([('Allen', 912), ('Jack', 910), ('David', 932)])
    print(dict1)

    dict2 = dict(Allan=912, Jack=910, David=932)
    print(dict2)

    dict3 = {x: x**2 for x in (2, 4, 6)}
    print(dict3)

def _loop():
    tel = dict(Allan=912, Jack=910, David=932)
    for k, v in tel.items():
        print(k, v)

    for i, (k, v) in enumerate(tel.items()):
        print(i, k, v)

    names = ['Allan', 'Jack', 'David']
    nums = [912, 910, 932]
    for name, num in zip(names, nums):
        print(f'name: {name}, num: {num}')

    for i in reversed(range(5)):
        print(i)

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for b in basket:
        print(b, end=', ')
    print()
    for b in sorted(basket):
        print(b, end=', ')
    print()
    for b in sorted(set(basket)):
        print(b, end=', ')
    print()

    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
    print(filtered_data)

def _cond():
    string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
    non_null = string1 or string2 or string3
    print(non_null)

def _other():
    print(f'(1, 2, 3) < (1, 2, 4): {(1, 2, 3) < (1, 2, 4)}')
    print(f'[1, 2, 3] < [1, 2, 4]: {[1, 2, 3] < [1, 2, 4]}')
    print(f"'ABC' < 'C' < 'Pascal' < 'Python':{'ABC' < 'C' < 'Pascal' < 'Python'}")
    print(f'(1, 2, 3, 4) < (1, 2, 4): {(1, 2, 3, 4) < (1, 2, 4)}') #3<4
    print(f'(1, 2) < (1, 2, -1):{(1, 2) < (1, 2, -1)}')#因為 (1,2) 是 (1,2,-1) 的前綴
    print(f'(1, 2, 3) == (1.0, 2.0, 3.0):{(1, 2, 3) == (1.0, 2.0, 3.0)}')
    print(f"(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4):{(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)}")
    #'aa' < 'abc'，因為 'aa' 是 'abc' 的前綴，且 aa < abc

if __name__ == "__main__":
    main()