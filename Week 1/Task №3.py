def zeros(n):
    import math
    s = 0
    while n > 1:
        s += math.floor(n / 5)
        n /= 5
    return s

assert zeros(454021874) == 113505460
assert zeros(201) == 49
assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(12) == 2
assert zeros(30) == 7
assert zeros(16) == 3

