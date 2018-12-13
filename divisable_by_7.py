"""question 1"""
def divisable():
    values = range(2000, 3201)

    value_list = []
    for value in values:
        if value % 7 == 0 and value % 5 != 0:
            value_list.append(value)

    return value_list
print(divisable())
