def is_prime(numb):
    if numb == 2:
        return True
    for i in range(2, numb):
        if numb % i == 0:
            return False
            continue
        else:
            return True


lst = []


# def prime(begin, end):
#     global lst
#     for i in range(begin, end+1):
#         if is_prime(i):
#             lst.append(i)
#     return lst


# print(prime(1, 9))

# def is_prime(numb):
#     for idx in range(2, numb):
#         if idx % idx == 0:
#             return False
#     return True


print(is_prime(100))