# lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = [1, 2, 3, 4, 5]
# lst = [1]
# lst = []

if len(lst) == 0:  # Перевірка порожнього списку
    b = [[], []]
    print (b)
elif len(lst) % 2 == 0:  # Перевірка парної кількості елементів
    split_lst = len(lst) // 2
    first_half = [lst[:split_lst], lst[split_lst:]]
    print(first_half)
else:  # Непарна кількість елементів
    split_lst = len(lst) // 2 + 1
    second_half = [lst[:split_lst], lst[split_lst:]]
    print (second_half)
