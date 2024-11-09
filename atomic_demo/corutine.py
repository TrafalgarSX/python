from collections.abc import Iterable, Iterator, Generator

# 实现了yield的函数
def mygen(n):
    now = 0
    line = ''
    while now < n:
        with open('text.txt', 'r') as f:
            line = f.readline() 
        yield line 
        now += 1

def mycorutine(n):
    now = 0
    line = ''
    file_path = 'text.txt'
    while now < n:
        with open(file_path, 'r') as f:
            line = f.readline() 
        file_path = yield line 
        if file_path is None:
            file_path = 'text.txt'
        now += 1

def testmycorutine():
    gen = mygen(10)
    # 使用列表生成式，注意不是[]，而是()
    print(isinstance(gen, Generator))  # True

    str = next(gen) 
    print(str)

    with open('text.txt', 'a') as f:
        f.write('guoyawen\n')

    print(next(gen))  # hello world1


    corutine = mycorutine(3)
    print(next(corutine))
    str = 'args.py'
    print(corutine.send(str))

def multiyeild():
    yield 'a'
    yield 'b'
    yield 'c'

def multiyeidlthrow():
    gmy = multiyeild()
    print(next(gmy))
    print(next(gmy))
    print(gmy.throw(StopIteration))
    print(next(gmy))


if __name__ == '__main__':
    multiyeidlthrow()






