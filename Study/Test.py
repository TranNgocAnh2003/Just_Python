
# 1.In ra cac so chia het cho 7 va ko la boi so cua 5

count = 0 
my_list=[]
for x in range(2000,3000):
    if (x % 7==0) and (x % 5 != 0):
        my_list.append(str(x))
    count += 1  
print(','.join(my_list))
print(count)


#2.Tinh giai thua

while True:
    x = int(input('Nhap so: '))
    def fact(x):
        if x == 1: return 1
        else:
            return x * fact(x-1)
    print(fact(x))


#3.Viet chuong trinh tao ra dictionary chua (i,i*i)

x = 8
d = dict()
for i in range(1, x + 1):
    d[i]=i*i
print(d)


#4.Viet chuong trinh nhap vao day so dau ra la mot list va tuple

x = '34L67L55L33L12L98'
l=x.split("L") # Chuyen x thanh mot list cach nhau boi ('L') L co the thay bang gi dao cx duwoc
t = tuple(l)
print(l)
print(t)

#5.Tinh gia tri binh phuong cua mot so
#C1
x = 8
print(x*x)


#C2 
def square(x):
    return x ** 2

print(square(x))

''' # END









