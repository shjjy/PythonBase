import sys


def main():
    print(_divide_numbers(10, 0))
    print(_divide_numbers(10, 2))
    _class()
    _variable()
    _common()
    _else() #沒有發生異常時才執行，進一步處理成功後的動作
    _change()
    _none()
    _finally() #無論有沒有異常都要執行，釋放資源
    _with_res()
    _note()
    _custom_class()

def _divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"錯誤：{e}")
        return None  #
    except Exception as e:
        print(f"發生未知錯誤：{e}")
        return None
    return result

def _class():
    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

    for cls in [B, C, D]:
        try:
            raise cls()
        except B:
            print("B")
        except C:
            print("C")
        except D:
            print("D")

def _variable():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        x, y = inst.args
        print('x =', x)
        print('y =', y)

def _common():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error:", err)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def _else():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

def _change():
    try:
        _some_err()
    except ConnectionError as exc:
        raise RuntimeError('Failed to open database') from exc

def _some_err():
    raise ConnectionError

def _none():
    try:
        open('database.sqlite')
    except OSError:
        raise RuntimeError from None

def _finally():
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')

def _with_res():
    with open("myfile.txt") as f:
        for line in f:
            print(line, end="")

def _note():
    try:
        raise TypeError('bad type')
    except Exception as e:
        e.add_note('Add some information')
        e.add_note('Add some more information')
        raise

def _custom_class():
    class MyCustomError(Exception):

        def __init__(self, message="發生錯誤"):
            self.message = message
            super().__init__(self.message)

    def divide(a, b):
        if b == 0:
            raise MyCustomError("除數不能為 0！")
        return a / b

    try:
        result = divide(10, 0)
    except MyCustomError as e:
        print(f"捕獲自訂錯誤: {e}")

if __name__ == "__main__":
    main()