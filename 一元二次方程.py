#解一元二次方程的公式法
print("================")
print("================")
print("================")
a=int(input("一元二次方程的a的值:"))
b=int(input("一元二次方程b的值:"))
c=int(input("一元二次方程c的值:"))

v= b ** 2 - 4 * a * c
print(str("跌塔的值:") + str(v))
x=(-b + v ** 1 / 2)/(2 * a)
print(str("第一个解:") + str(x))
xor=(-b - v ** 1/2)/(2 * a)
print(str("第二个解：") + str(xor))
print("================")
print("================")
print("================")
print('author:刘俊伟')
