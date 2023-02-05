a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        nonlocal a 
        print(a)
    return inner_function()

print(enclosing_funcion())
