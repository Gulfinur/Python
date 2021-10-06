a = float(input("Введите делитель: "))
b = float(input("Введите делимое: "))
def fec(arg1, arg2):
    if arg2 == 0:
        return print("На ноль делить нельзя")
    else: return arg1/arg2
print(fec(a, b))
