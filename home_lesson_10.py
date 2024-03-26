import string
import keyword

name = 'чфт вук'

if name[0].isdigit(): # Перевірка, на першу цифру
        print (False)
elif name.isdigit():     # Перевірка, чи складається тільки з цифр
    print(False)
    # Перевірка, чи містить великі літери, пропуск або знаки пунктуації (крім нижнього підкреслення)
elif any(char in string.punctuation.replace("_", "") or char.isupper() or char.isspace() for char in name):
    print(False)
elif name in keyword.kwlist:  # Перевірка, чи не є зарезервованим словом
    print(False)
else:
    print(True)



