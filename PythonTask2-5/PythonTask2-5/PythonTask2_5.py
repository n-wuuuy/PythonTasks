from typing import Tuple

def get_digits(num: int) -> Tuple[int]:
    return tuple([int(a) for a in str(num)])

print(get_digits(87178291199))

