def int32_to_ip(int32):
    temp = format(int32, 'b')
    temp = '0' * (32 - len(temp)) + temp
    ip = ''
    for octet in range(0, len(temp), 8):
        ip += str(int(temp[octet:octet + 8], base=2)) + '.'
    return ip[:-1]


assert int32_to_ip(32) == "0.0.0.32"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"