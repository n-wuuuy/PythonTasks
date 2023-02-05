

def call_once(orig_func):
    a=True
    def wrapper(*args):
        nonlocal a
        if a:
            a=False
            return orig_func(*args)
        else:return exit()
    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
sum_of_numbers(13, 42)
sum_of_numbers(13, 42)