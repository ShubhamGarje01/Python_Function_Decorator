#  two times enhancing same function

def decor(num):
    def inner():
        a = num()
        multi = a * 5
        return multi
    return inner


def decor1(num):
    def inner():
        b = num()
        add = b + 5
        return add
    return inner


def num():
    return 10


num = decor1(decor(num))
print(num())
