lst = [0, 1, 0, 12, 3]
# [0]
# [1, 0, 13, 0, 0, 0, 5]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

zeros = []
non_zeros = []

for num in lst:
    if num == 0:
        zeros.append(num)
    else:
        non_zeros.append(num)

print(non_zeros+zeros)