def bananas(s) -> set:
    banana = 'banana'
    if len(s) >= len(banana):
        return search_banana(s, banana)
    return set()


def search_banana(s, banana):
    result = list()
    if banana == '':
        result.append(''.rjust(len(s), '-'))
        return result
    for i in range(len(s)):
        if banana[0] == s[i]:
            head = ''.rjust(i, '-') + s[i]
            if s[i+1:] == '' and banana[1:] == '':
                result.append(head)
            else:
                arr = search_banana(s[i+1:], banana[1:])
                for tail in arr:
                    result.append(head + tail)
    if result == '':
        result = set()
    return set(result)


assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
assert bananas("banann") == set()
