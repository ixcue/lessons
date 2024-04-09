import string

name = input('Введите строку: ')
name = name.title().replace(' ','')
for p in string.punctuation:
    name.replace(p,'')
name = f'#{name}'[:140]

print(name)






