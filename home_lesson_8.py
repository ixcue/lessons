# lst = [0, 1, 0, 12, 3]
lst = []
# [1, 0, 13, 0, 0, 0, 5]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

a = 0
if len(lst) == 0:  # Перевірка порожнього масиву
    lst = 0
    print(lst)

else:
    for num in lst:
        if num % 2 == 0:
            a += num
    b = a * lst[-1]
    print(b)