list = []
for i in range(1, 1001, 2):
    list.append(i ** 3)
c = 0
for k in range(len(list)):
    b = 0
    a = str(list[k])
    for j in range(len(a)):
        a = str(list[k])
        a1 = int(a[j])
        b += a1
    if (b % 7) == 0:
        c += int(a)  # сумма чисел, кратных 7

print(c)

for i in range(len(list)):
    list[i] += 17

c = 0
for k in range(len(list)):
    b = 0
    a = str(list[k])
    for j in range(len(a)):
        a = str(list[k])
        a1 = int(a[j])
        b += a1
    if (b % 7) == 0:
        c += int(a)

print(c)
