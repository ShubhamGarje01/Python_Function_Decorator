def characters(numbers):  # this is function decorator in this case
    def both():  # this is inner function (nested function)
        print("A", " B", " C", " D", " E")
        numbers()
        print("a, b, c, d, e")
    return both


@characters
def numbers():
    print("1, 2, 3, 4, 5")


numbers()
