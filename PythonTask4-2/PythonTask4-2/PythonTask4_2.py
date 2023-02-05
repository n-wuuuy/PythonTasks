from collections import Counter


def most_common_words(filepath, number_of_words=3):
    file=open(filepath,'r')
    s=str(file.read().splitlines())
    chars = ["!",".","'",'"',",","[","]"]
    s = s.translate(str.maketrans('', '', ''.join(chars)))
    line_word = s.lower().split(" ");
    ls=Counter(line_word)
    f=[]
    ls.pop('')
    for a in range(number_of_words):
        f.append(max(ls, key=ls.get))
        ls.pop(max(ls, key=ls.get))
        file.close()
    return f


print(most_common_words('lorem_ipsum.txt'))