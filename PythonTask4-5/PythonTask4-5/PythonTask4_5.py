
def remember_result(orig_func):
    resl=None
    def wrapper(*rargs):
        nonlocal resl
        print(f"Last result = '{resl}'")
        resl=''
        for item in rargs:
            resl += item
        resoult=orig_func(*rargs)
        return resoult
    return wrapper

@remember_result
def sum_list(*args):
    result=""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
sum_list("abc", "cde")