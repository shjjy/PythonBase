
def main():
    _num()
    _string()
    _list()
    _fib_seq()

def _num():
    width = 20
    height = 5 * 9
    print(width * height)
    print(5 ** 2)

def _string():
    print('doesn\'t')
    print("doesn't")
    print('"Yes," they said.')
    print("\"Yes,\" they said.")
    s = 'First line.\nSecond line.'
    print(s)
    print('C:\some\name')
    print(r'C:\some\name')
    text = ('Put several strings within parentheses '
            'to have them joined together.')
    print(text)
    prefix = 'Py'
    print(prefix + 'thon')

    word = 'Python'
    print(word[0])
    print(word[5])
    print(word[-6])
    print(word[-1])

    print(word[0:2])
    print(word[:2])

    #word[0] = 'J'

    print(len(word))

def _list():
    squares = [1, 4, 9, 16, 25]
    print(squares)
    print(squares[:3])
    print(squares[-3:])
    print(squares + [36,49])

    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64
    print(cubes)

    # 等於傳 Ref
    rgb = ["Red", "Green", "Blue"]
    rgba = rgb
    print(f"rgb, rgba 是否為同物件: {id(rgb) == id(rgba)}")
    rgba.append("Alph")
    print(rgb)

    #Slice 賦值，傳新 List
    correct_rgba = rgba[:]
    correct_rgba[-1] = "Alpha"
    print(f"correct_rgba {correct_rgba}")
    print(f"rgba {rgba}")
    print(len(rgba))

def _fib_seq():
    print('start fib...')
    a, b=0, 1
    while a<10:
        print(a, end=", ")
        a, b = b, a + b

if __name__ == "__main__":
    main()