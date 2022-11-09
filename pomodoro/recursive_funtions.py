# def sum(n):
#     result = 0
#     for i in range(n + 1):
#         result += i
#     return result
#
#
# print(f"result of sum of first 100 numbers is {sum(100)}")


def sum(n):
    if n > 0:
        return n + sum(n - 1)
    else:
        return 0


print(f"result of sum of first 100 numbers is {sum(100)}")
