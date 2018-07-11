x = 1
def scope():
    x = 3
    y = 10
    print(x)

scope()   # prints 3
print(y)  # poduces NameError


def scope2():
    print(x)

scope2()

def change_global_x():
    global x
    x = 3
    print(x)

change_global_x()
print(x)


