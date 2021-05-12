a = int(input("Введите число:  "))
b = str(a)
if (a >= 11) and (a <= 19):
    print(f"{a} процентов")
elif b[-1] == "1":
    print(f"{a} процент")
elif (b[-1] >= "2") and (b[-1] <= "4"):
    print(f"{a} процента")
else:
    print(f"{a} процентов")
