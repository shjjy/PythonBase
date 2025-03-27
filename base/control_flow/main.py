
def main():
    _if()
    _for()
    _range()
    _for_else()
    _pass()
    _match()
    _func()

def _if():
    x = int(input("Enter a number: "))
    if x < 0:
        x = 0
        print('Negative')
    elif x == 0:
        print('Zero')
    else:
        print('Positive')

def _for():
    seq = ['apple', 'boy', 'correlation']
    for w in seq:
        print(w, len(w))

    users = {'Allen': 'Active',
             'John': 'Inactive',
             'Louis': 'Active',
             '456@^': 'Error'}
    act_user = {}
    for k, v in users.items():
        if v == 'Active':
            act_user[k] = v
    print(act_user)

    users = {user:status for user, status in users.items()if status != 'Error'}
    print(users)

def _range():
    for i in range(5):
        print(i, end=', ')

    print()
    print(list(range(5, 10)))
    print(list(range(0, 10, 2))) #range(start, stop, step)

    users = ['apple', 'boy', 'correlation']

    for i in range(len(users)):
        print(i, users[i], end=', ')

    print()
    print(sum(range(4)))

def _for_else():
    for n in range(2, 10):
        for i in range(2, n):
            if n % i == 0:
                print(f'{n} = {i} * {n//i}')
                break
        else:
            print(f'{n} is prime')

def _pass():
    pass # 之後再補上函式內容

    class MyClass:
        def method(self):
            pass  # 先留空，之後再寫具體內容

    for i in range(5):
        pass  # 先保留，之後再填入邏輯

def _match():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Points:
        __match_args__ = ('x', 'y')  # 顯式設置哪些屬性參與匹配

        def __init__(self, x, y):
            self.x = x
            self.y = y

    def _http_error(status):
        match status:
            case 400:
                print('Bad Request')
            case 403:
                print('Forbidden')
            case 404:
                print('Not Found')
            case 401 | 402:
                print('Unauthorized')
            case _:
                print('Server Error')

    def _get_point(point):
        match point:
            case (0, 0):
                print("Origin")
            case (0, y):
                print(f"Y={y}")
            case (x, 0):
                print(f"X={x}")
            case (x, y):
                print(f"X={x}, Y={y}")
            case _:
                raise ValueError("Not a point")

    def _match_point(point):
        match point:
            case Points(x=0, y=0):
                print("Origin")
            case Points(x=0, y=y):
                print(f"Y={y}")
            case Points(x=x, y=0):
                print(f"X={x}")
            case Points():
                print("Somewhere else")
            case _:
                print("Not a point")

    def _match_points(points):
        match points:
            case []:
                print("No points")
            case [Points(0, 0)]:
                print("The origin")
            case [Points(x, y)] if x == y:  # 注意這裡變成檢查列表中的元素
                print(f"Y=X at {x}")
            case [Points(x, y)]:
                print(f"Single point {x}, {y}")
            case [Points(0, y1), Points(0, y2)]:
                print(f"Two on the Y axis at {y1}, {y2}")
            case _:
                print("Something else")

    _http_error(401)
    _get_point((3, 0))
    _match_point(Point(1, 0))

    points = [Points(0, 3), Points(0, 4)]
    _match_points(points)

    points2 = [Points(2, 2)]
    _match_points(points2)

def _func():

    def _get_fib(n):
        result = []
        a,b = 0,1
        while a<n:
            result.append(a)
            a, b = b, a+b
        return result

    def _kid_bmi(a, h=1.2, w=23):
        print(f'age = {a}, BMI = {w/h/h}')

    def _func_pos(a, b, /, c, *, d, e):
        print(a, b, c, d, e)

    def _func_add(*args):
        exp = " + ".join(map(str, args))
        total = sum(args)
        print(f'{exp} = {total}')
        return total

    def _func_kwargs(**kwargs):
        for k, v in kwargs.items():
            print(f'{k} = {v}')

    def _func_kwargs2(**kwargs):
        for person, details in kwargs.items():
            print(f'{person}')
            for k, v in details.items():
                print(f' {k} = {v}')

    def _func_unpacking_mul(a, b, c):
        return a*b*c

    def _func_unpacking_person(name, age, city):
        print(f'name = {name}, age = {age}, city = {city}')

    def _func_lamda():
        add = lambda a, b: a + b
        print(add(1, 2))
        f = _func_for_lamda(10)
        print(f(1))

        pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
        pairs.sort(key=lambda pair: pair[1])
        print(pairs)

    def _func_for_lamda(n):
        return lambda x: x + n

    def _func_doc():
        """Do nothing, but document it.

        No, really, it doesn't do anything.
        """
        pass

    def _func_annotation(ham: str, eggs: str = 'big eggs') -> str:
        print("Annotations:", _func_annotation.__annotations__)
        print("Arguments:", ham, eggs)
        return ham + ' and ' + eggs

    def _func_annotation2(ham: str, eggs: str = 'big eggs') -> str:
        """
        函式將兩個字串合併並回傳。

        Args:
            ham (str): 代表火腿的字串。
            eggs (str, optional): 代表蛋的字串，預設為 'big eggs'。

        Returns:
            str: 合併後的字串，格式為 "ham and eggs"。
        """
        return ham + ' and ' + eggs

    print(_get_fib(100))
    _kid_bmi(12)
    _kid_bmi(a=12)
    _kid_bmi(h=1.3, a=13)
    _func_pos(1, 2, 3, d=4, e=5)  # 斜線前不能用 keyword
    _func_pos(1, 2, c=3, d=4, e=5)  # 星號後一定要用 keyword

    print(_func_add(1, 2, 3))
    _func_kwargs(name='Yang', age=40, city='kaohsiung')
    people = {
        "p1": {"name": "A", "age": 29, "city": "kaohsiung"},
        "p2": {"name": "B", "age": 39, "city": "taipei"}
    }
    _func_kwargs2(**people)

    print(_func_unpacking_mul(2, 3, 4))
    nums = [2, 3, 4]
    print(_func_unpacking_mul(*nums))

    people2 = [
        {"name": "A", "age": 29, "city": "kaohsiung"},
        {"name": "B", "age": 39, "city": "taipei"}
    ]
    for p in people2:
        _func_unpacking_person(**p)

    _func_lamda()
    _func_doc()
    print(_func_annotation('spam'))
    print(_func_annotation2('spam'))

if __name__ == "__main__":
    main()