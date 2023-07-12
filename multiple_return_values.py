def arithmetic(num_1, num_2):
    add = num_1+num_2
    sub = num_1-num_2
    mult = num_1*num_2
    div = num_1/num_2
    # return the values
    return add, sub, mult, div


a, b, c, d = arithmetic(20, 2)
print("add:", a)
print("sub:", b)
print("mult:", c)
print("div:", d)
