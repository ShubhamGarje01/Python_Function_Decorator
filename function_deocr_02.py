# Que:- function returning 10 make it 15 without modifying that function

def modify(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner


# @modify
def num():
    return 10


num = modify(num)
print(num())
