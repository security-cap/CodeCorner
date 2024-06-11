def a():
        print('a() starts')
        b()
        d()
        print('a() returns')
def b():
        print('b() starts')
        c()
        print('b() returns')
def c():
        print('c() start')
        print('c() returns')
def d():
        print('d() start')
        print('d() return')
a()