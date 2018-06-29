
num = input('>>>:')


def inner():
    c = 0
    for i, v in enumerate(num):
        a = int(v) ** 2
        c += a
    return c
res = inner()
print(res)


