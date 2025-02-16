def rttd(number, max_degress):
    i = 0
    for _ in range(max_degress):
        yield number ** i
        i += 1
res = rttd(122345, 500)
for _ in res:
    print(_, "\n")