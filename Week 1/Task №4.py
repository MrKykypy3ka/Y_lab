def bananas(s) -> set:
    import itertools
    result = list()
    banana = 'banana'
    if len(s) >= len(banana):
        variants = list(itertools.permutations(list('-' * (len(s) - len(banana)) + '.' * len(banana)), len(s)))
        for elem in variants:
            temp = ''
            for i in range(len(elem)):
                if elem[i] == '.':
                    temp += s[i]
                else:
                    temp += elem[i]
            if temp.replace('-', '') == banana and temp not in result:
                result.append(temp)
    if result == '':
        result = set()
    return set(result)




assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
