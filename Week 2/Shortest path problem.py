def shortest_way(addresses):
    import math
    import itertools
    s = dict()
    for elem in itertools.permutations(list(addresses.keys())[1:], len(addresses.keys()) - 1):
        x = tuple(['Почтовое отделение'] + list(elem) + ['Почтовое отделение'])
        s[x] = list()
        for i in range(1, len(x)):
            s[x].append(math.sqrt((addresses[x[i]][0] - addresses[x[i-1]][0]) ** 2 + (addresses[x[i]][1] - addresses[x[i-1]][1]) ** 2))
    result = [min(s, key=s.get), min(s.values())]
    for i in range(len(result[0]) - 1):
        print(f'{addresses[result[0][i]]} -> {addresses[result[0][i+1]]} = [{sum(result[1][0:i+1])}]', end='  ')


shortest_way({'Почтовое отделение': (0, 2),
              'Ул. Грибоедова, 104/25': (2, 5),
              'Ул. Бейкер стрит, 221б': (5, 2),
              'Ул. Большая Садовая, 302-бис': (6, 6),
              'Вечнозелёная Аллея, 742': (8, 3)})