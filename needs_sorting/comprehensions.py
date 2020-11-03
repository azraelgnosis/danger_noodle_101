def print_list(lst):
    pass

a = []
for i in range(10):
    a.append(i)

b = [i for i in range(10)]

assert a == b

nested = [[j for j in range(10)] for i in range(10)]