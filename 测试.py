#解一元二次方程的公式法
print("================")
print("================")
print("================")
a=int(input("一元二次方程的a的值:"))
b=int(input("一元二次方程b的值:"))
c=int(input("一元二次方程c的值:"))
v= b ** 2 - 4 * a * c
x=(-b + v ** 1 / 2)/(2 * a)
xor=(-b - v ** 1/2)/(2 * a)
print(str("跌塔的值:") + str(v))
if v>=0:
    print("第一个解:")+tr(x)

    print("第二个解:")+str(xor)

else:
    print('此方程无实数根')

print("================")
print("================")
print("================")
print('author:刘俊伟')
