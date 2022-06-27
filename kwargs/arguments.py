# def add(*args):
#     return sum(args)
# def max_fun(*args):
#     return max(args)
# def min_fun(*args):
#     return min(args)
#
#
# print(add(10,20))
# print(add(10,20,30))
# print(max_fun(10,20,30))
# print(min_fun(10,20,30))


def add_nums(**kwargs):
    print(kwargs)
add_nums(n1=10,n2=20,n3=30)


def add_nums(**kwargs):
    print(sum([v for k,v in kwargs.items()]))
    print(sum([v for  v in kwargs.values()]))
add_nums(n1=10,n2=20,n3=30)