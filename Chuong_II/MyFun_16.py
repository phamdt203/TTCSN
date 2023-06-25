def MyFun(x):
    x[0] = 20

lst = [10, 11, 12, 13, 14, 15]
MyFun(lst)
print(lst) # [20, 11, 12, 13, 14, 15]