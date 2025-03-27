import json
import math

def main():
    _output()
    _format()
    _format_method()
    _file()

def _output():
    yes_votes = 42_572_654
    total_votes = 85_705_149
    percentage = yes_votes / total_votes
    print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))#- 左邊對其，最少9個字符

    s = 'Hello, world.'
    print(str(s))
    print(repr(s))

    hello = 'hello, world\n'
    hellos = repr(hello)
    print(hellos)

def _format():
    print(f'The value of pi is approximately {math.pi:.3f}.')#f:float

    map = {"Allan": 910, "Bill": 912, "David": 932}

    for name, number in map.items():
        print(f'name: {name:10}, number: {number:10d}')#d:decimal integer

    animals = 'eels'
    print(f'My hovercraft is full of {animals!s}.') #!s => str()
    print(f'My hovercraft is full of {animals!r}.') #!r => repr

    bugs = 'roaches'
    count = 13
    area = 'living room'
    print(f'Debugging {bugs=} {count=} {area=}')

def _format_method():
    print('We are the {} who say "{}!"'.format('knights', 'Ni'))

    print('{0} and {1}'.format('spam', 'eggs'))
    print('{1} and {0}'.format('spam', 'eggs'))

    print('This {food} is {adjective}.'.format(
        food='spam', adjective='absolutely horrible'))

    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
          'Dcab: {0[Dcab]:d}'.format(table))

    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))

    students = [
        {"name": "Alice", "score": 85, "rank": 3},
        {"name": "Bob", "score": 92, "rank": 1},
        {"name": "Charlie", "score": 78, "rank": 5},
        {"name": "David", "score": 88, "rank": 2},
        {"name": "Eve", "score": 80, "rank": 4}
    ]

    students = sorted(students, key=lambda x: x["rank"])

    print("=" * 32)
    print(" 成績報告 ".center(30, "="))  # center 置中顯示標題
    print("=" * 32)

    # 印出表頭
    print("排名".ljust(6), "姓名".ljust(10), "分數".rjust(6))

    print("-" * 32)

    # 印出學生成績
    for student in students:
        rank = str(student["rank"]).zfill(6)  # zfill 讓排名補 0
        name = student["name"].ljust(10)  # ljust 讓姓名左對齊
        score = str(student["score"]).rjust(6)  # rjust 讓分數右對齊
        print(rank, name, score)

    print("=" * 32)

def _file():
    students = [
        {"name": "Alice", "score": 85, "rank": 3},
        {"name": "Bob", "score": 92, "rank": 1},
        {"name": "Charlie", "score": 78, "rank": 5},
        {"name": "David", "score": 88, "rank": 2},
        {"name": "Eve", "score": 80, "rank": 4}
    ]
    students = sorted(students, key=lambda x: x["rank"])

    # **寫入 JSON 檔案**
    score_filename = "students.json"
    with open(score_filename, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)

    print(f"已將學生資料寫入 {score_filename}")

    # **讀取 JSON 檔案**
    with open(score_filename, "r", encoding="utf-8") as file:
        loaded_students = json.load(file)

    print("讀取到的學生資料：")
    for student in loaded_students:
        print(f"姓名: {student['name']}, 分數: {student['score']}, 排名: {student['rank']}")


    filename = "students.txt"
    # 使用 f.write 寫入資料
    with open(filename, "w", encoding="utf-8") as f:
        for student in students:
            f.write(f"姓名: {student['name']}, 分數: {student['score']}, 排名: {student['rank']}\n")

    print(f"已將學生資料寫入 {filename}")

    # 讀取檔案
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    print("讀取到的學生資料：")
    print(content)

if __name__ == "__main__":
    main()