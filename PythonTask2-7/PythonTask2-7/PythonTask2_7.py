import math
from typing import List

def foo(num:List[int]) -> List[int]:
    return [math.prod(num)/a for a in num]


print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))
