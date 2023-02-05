from typing import List
from typing import Tuple


def get_pairs(lst: List) -> List[Tuple]:
    if(len(lst))<2:return None
    return [tuple([i,j]) for i,j in zip(lst[:-1],lst[1:])]

print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))