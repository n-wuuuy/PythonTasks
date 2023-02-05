

from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    slovo=[s[i:j] for i,j in zip([0]+indexes,indexes+[len(s)])]
    if '' in slovo:
        slovo.pop()
    return slovo

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))

print(split_by_index("no luck", [42]))


