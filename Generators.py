def feed(l):
    yield l
l = ['1..100','200..300','300..400']
load = feed(l)
print(next(load))


def feed(l):
    for i in l:
        yield i
l = ['1..100','200..300','300..400']
load = feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))
print(next(load))


def count_up_ton(
