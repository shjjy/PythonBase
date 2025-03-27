import bisect
import doctest
import gc
import locale
import logging
import pprint
import reprlib
import textwrap
import threading
import timeit
import math
import os
import random
import re
import statistics
import sys
import weakref
import zipfile
from array import array
from collections import deque

from datetime import date
from decimal import Decimal, getcontext
from heapq import heapify, heappush, heappop
from string import Template

def main():
    _os()
    _sys()
    _re()
    _math()
    _datetime()
    _performance()
    print(_doctest_average([10, 20]))
    _output_format()
    _templating()
    _multi_thread()
    _logging()
    _weak_ref()
    _list_tool()
    _decimal()

def _os():
    print(os.getcwd())
    os.system('mkdir test_folder')
    print(dir(os))

def _sys():
    print(f'sys.argv: {sys.argv}')
    sys.stderr.write('Warning, log file not found starting a new one\n')

def _re():
    print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

def _math():
    print(f'Log base 2 of 1024 is {int(math.log(1024, 2))}')

    print('random choice: ' + random.choice(['apple', 'pear', 'banana']))

    print(f'random num 0~99: : {random.sample(range(100), 2)}')

    print(f'random 0~1: {random.random()}')

    print(f'1 到 9 之間的奇數: {random.randrange(1, 10, 2)}')#random.randrange(start, stop, step)

    print(f'randrange 0~5隨機會重複{[random.randrange(6) for i in range(6)]}')

    print(f'sample 0~5隨機會不重複{random.sample(range(6), 6)}')

    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    print(f'statistics mean: {statistics.mean(data)}, median: {statistics.median(data)}, '
          f'variance: {statistics.variance(data)}, stdev: {statistics.stdev(data)}')

def _datetime():
    now = date.today()
    print(f'today: {now}')
    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
    my_bitrhday = date(1985, 1, 1)
    age = now - my_bitrhday
    print(f'age: {age.days/365}')

def _performance():
    def _sum_to_1000():
        return sum(range(1000))

    execution_time = timeit.timeit(_sum_to_1000, number=1000)
    print(f'執行時間: {execution_time} 秒')

def _doctest_average(values):
    return sum(values) / len(values)

def _output_format():
    print(reprlib.repr(set('supercalifragilisticexpialidocious'))) #...省略

    t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
    pprint.pprint(t, width=30) #印出結構

    doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
    the wrapped lines."""
    print(textwrap.fill(doc, width=40))

    print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))

    conv = locale.localeconv()  # get a mapping of conventions
    x = 1234567.8
    print(locale.format_string("%d", x, grouping=True))
    print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True))

def _templating():
    t = Template('${village} folk send $$10 to $cause.')
    print(t.substitute(village='Nottingham', cause='the ditch fund'))

def _multi_thread():
    class AsyncZip(threading.Thread):
        def __init__(self, infile, outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile

        def run(self):
            f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
            print('Finished background zip of:', self.infile)

    background = AsyncZip('mydata.txt', 'myarchive.zip')
    background.start()
    print('The main program continues to run in foreground.')

    background.join()  # 等待背景任務結束
    print('Main program waited until background was done.')

def _logging():
    logging.debug('Debugging information')
    logging.info('Informational message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error -- shutting down')

def _weak_ref():
    class A:
        def __init__(self, value):
            self.value = value

        def __repr__(self): # 回傳適合開發者閱讀的字串，print(repr(a))  # A(10)（開發者用）
            return str(self.value)
    a = A(10)  # 創建一個 A(10) 的物件並指派給變數 a
    d = weakref.WeakValueDictionary()
    d['primary'] = a  # 將 a 放入字典，但不會增加其參考計數
    print(d['primary'])

    del a  # 刪除 a，移除對 A(10) 的強參考
    gc.collect()
    print(d['primary'])

def _list_tool():
    a = array('H', [4000, 10, 700, 22222]) #H typecode:0~ˊ65535
    print(sum(a))
    print(a[1:3])

    d = deque(["task1", "task2", "task3"])
    d.append("task4")
    print("Handling", d.popleft())

    scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
    bisect.insort(scores, (300, 'ruby'))
    print(scores)#操作 sorted list

    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    heapify(data)  # 轉換成最小堆
    heappush(data, -5)  # 插入新元素 -5
    print([heappop(data) for i in range(3)])

def _decimal():
    print(round(Decimal('0.70') * Decimal('1.05'), 2))
    print(round(.70 * 1.05, 2))

    print(Decimal('1.00') % Decimal('.10'))
    print(1.00 % 0.10)

    print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
    print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0)

    getcontext().prec = 5
    print(Decimal(1) / Decimal(7))

if __name__ == "__main__":
    main()
    # doctest.testfile("test_cases.txt", verbose=True)