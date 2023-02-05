def count_letters(s):
    return {a: s.count(a) for a in s }

print(count_letters("stringsample"))