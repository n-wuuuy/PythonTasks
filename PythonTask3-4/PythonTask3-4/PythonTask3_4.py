from collections import Counter

def combine_dicts(*args):
    keys = set()
    for arg in args:
        keys = keys.union(arg.keys())
    return {k: sum([arg.get(k,0) for arg in args]) for k in keys}



dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}


print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))

