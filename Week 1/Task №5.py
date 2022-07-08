def count_find_num(primesL, limit):
    import itertools
    import math
    result = list()
    if (x := math.prod(primesL)) == limit:
        result.append(x)
    elif x <= limit:
        result.append(x)
        temp = list()
        for i in range(1, 25):
            temp += list(itertools.combinations_with_replacement(primesL, i))
        for elem in temp:
            if (y := math.prod(elem) * x) <= limit:
                result.append(y)
    if (l := len(result)) == 0:
        return result
    return [l, max(result)]



primesL = [2, 5, 7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []