import string

def test_1_1(*strings):
    return set.intersection(*map(set,strings))

def test_1_2(*strings):
    return set.union(*map(set,strings))

def test_1_3(*strings):
    return set.union(*map(set,[set(strings[0]).intersection(set(strings[a+1])) for a in range(len(strings)-1)]))

def test_1_4(*strings):
    return set.difference(set(string.ascii_lowercase),*map(set,strings))

a=["hello","world","python"]
print(test_1_1("hello","world","python"))
print(test_1_2("hello","world","python"))
print(test_1_3("hello","world","python"))
print(test_1_4("hello","world","python"))