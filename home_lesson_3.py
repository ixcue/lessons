a = int(input('Введіть 5-ти значне число:'))
b = a % 10
c = a // 10 % 10
d = a // 100 % 10
e = a // 1000 % 10
f = a // 10000
print (f*1+e*10+d*100+c*1000+b*10000)