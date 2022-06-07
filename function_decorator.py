def decore(arg):
    def inner():
        print("Before...")
        arg()
        print("After...")
    return inner


@decore  # always written before the function def which we want to enhance.
def num():
    print("hii this is the main function")
    print("we want to modify this function without modifying actual code")


# num = decore(num)  # uncomment this and commend @decore both are same just position is different.
num()  # because we want to enhance same function that`s why we use same name
