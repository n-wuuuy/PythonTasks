
def get_shortest_word(s: str) -> str:
    return [a for a in s.split(" ") if len(a)== max(map(lambda x:len(x),s.split(" ")))][0]


print(get_shortest_word('Any pythonista like namespaces a lot.'))
print(get_shortest_word('Python is simple and effective.'))


