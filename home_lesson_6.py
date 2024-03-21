#lst = [12, 3, 4, 10]
# [1]
#lst = []
lst = [12, 3, 4, 10, 8]

# if len(lst) <= 1:  # Перевірка порожнього списку або списку з одним елементом
#     print(lst)
# else:
#     result_lst = lst[:-1] # Створюємо новий список, в який копіюємо всі елементи, крім останнього
#     last_element = lst[-1]
#     result_lst.insert(0, last_element)    # Додаємо останній елемент на початок нового списку
#     print(result_lst)

if lst:  #альтернативний варіант
    lst.insert(0,lst.pop(-1))
print(lst)

