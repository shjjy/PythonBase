from dataclasses import dataclass


def main():
    #本質像字典
    _class_obj()
    _instance_()
    _instance_var()
    _remark()
    _self_call()
    _inheritance()
    _multi__inheritance()
    _private_method_inheritance()
    _dataclass()
    _iterator()
    _generator()

def _class_obj():
    class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart
    x = Complex(3, 4)
    print(x)
    print(x.r)
    print(x.i)

def _instance_():
    class MyClass:
        #__slots__ = ['i'], 可以避免動態生成參數 counter
        i = 12345
        def f(self):
            return 'hello world'

        @staticmethod
        def static_method():
            return "這是靜態方法，不需要 self"

        @classmethod
        def get_count(cls):
            return cls.i  # 訪問類別變數，不用 self

    x = MyClass()
    xf = x.f()
    for i in range(2):
        print(xf)
    print(x.static_method())
    print(x.get_count())

    x.counter = 1
    while x.counter < 10:
        x.counter = x.counter * 2
    print(x.counter)
    del x.counter

def _instance_var():
    class Dog:
        kind = 'canine'

        def __init__(self, name):
            self.name = name

    class CommonDog:  # 所有實例共享 tricks 屬性
        tricks = []

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)

    class SelfDog:  # 每個實例有自己的 tricks 屬性
        def __init__(self, name):
            self.name = name
            self.tricks = []  # 每個物件的 tricks 是獨立的

        def add_trick(self, trick):
            self.tricks.append(trick)

    df = Dog('Fido')
    db = Dog('Buddy')
    print(f'Dog F kind:{df.kind}')
    print(f'Dog B kind:{db.kind}')
    print(f'Dog F name:{df.name}')
    print(f'Dog B name:{db.name}')

    cf = CommonDog('Fido')
    cb = CommonDog('Buddy')
    print(f'CommonDog F add trick:{cf.add_trick('roll over')}')
    print(f'CommonDog B add trick:{cb.add_trick('play dead')}')
    print(f'CommonDog F tricks:{cf.tricks}')
    print(f'CommonDog B tricks:{cb.tricks}')

    sf = SelfDog('Fido')
    sb = SelfDog('Buddy')
    print(f'SelfDog F tricks:{sf.add_trick('roll over')}')
    print(f'SelfDog B tricks:{sb.add_trick('play dead')}')
    print(f'SelfDog F tricks:{sf.tricks}')
    print(f'SelfDog B tricks:{sb.tricks}')

def _remark():
    class Warehouse:
        purpose = 'storage'
        region = 'west'

    w1 = Warehouse()
    print(w1.purpose, w1.region)
    w2 = Warehouse()
    w2.region = 'east'
    print(w2.purpose, w2.region)

def _self_call():
    class Bag:
        def __init__(self):
            self.data = []

        def add(self, x):
            self.data.append(x)

        def addTwice(self, x):
            self.add(x)
            self.add(x)

    b = Bag()
    b.add([1, 2])
    b.addTwice([3, 4])
    print(b.data)

def _inheritance():
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "sound"

    class Dog(Animal):
        def speak(self):
            return "汪"

    class Cat(Animal):
        def speak(self):
            return "喵"

    class Bird(Animal):
        def __init__(self, name, wing_span):
            super().__init__(name)  # 呼叫父類的 __init__
            self.wing_span = wing_span

    dog = Dog("來福")
    cat = Cat("橘貓")
    bird = Bird("老鷹" , 2)
    print(f'{dog.name} : {dog.speak()}, {cat.name} : {cat.speak()}, {bird.name} : {bird.speak()} - {bird.wing_span}')

def _multi__inheritance():
    class Flyable:
        def fly(self):
            return "I can fly!"

    class Swimmable:
        def swim(self):
            return "I can swim!"

    class Duck(Flyable, Swimmable):
        pass  # 不需要額外定義，也會繼承 fly() 和 swim()

    duck = Duck()
    print(duck.fly())
    print(duck.swim())

def _private_method_inheritance():
    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)  # 仍然可以在這裡使用私有的 __update

        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)

        __update = update  # 讓 __update 保持原始的 update 行為

    class MappingSubclass(Mapping):
        def update(self, keys, values):
            for item in zip(keys, values):
                self.items_list.append(item)

    m = MappingSubclass(['a', 'b', 'c'])
    print(m.items_list)

def _dataclass():

    @dataclass
    class person:
        name: str
        age: int
        phone_number: str = "N/A"

    yang = person(name='yang', age=20)
    print(f'name:{yang.name}, age:{yang.age}, phone_number:{yang.phone_number}')

def _iterator():
    s = '123'
    it = iter(s)
    print(it)
    print(next(it))
    print(next(it))

    class Reverse:
        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]

    apple = Reverse('apple')
    it = iter(apple)
    for item in it:
        print(item)

def _generator():
    def reverse(data):
        for index in range(len(data) - 1, -1, -1):#range(start, stop, step)
            yield data[index]

    for char in reverse('apple'):
        print(char)

    print(sum(i*i for i in range(5)))
    print(sum(x*y for x in range(5) for y in range(5)))
    print(sum(x*y for x, y in zip([1, 2, 3], [10, 20, 30])))

    data = 'apple'
    print(list(data[i] for i in range(len(data) - 1, -1, -1)))

if __name__ == "__main__":
    main()