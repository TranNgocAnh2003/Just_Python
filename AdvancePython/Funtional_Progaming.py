#Pure Function
'''
def multi(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multi([1,2,3]))
'''
#map(), filter(), zip(), reduce()
my_list = [1,2,3,4,5]
your_list = [10, 20, 30, 40, 60, 70] 

from functools import reduce
def multiply_by2(item):
    return item*2

def check_odd(item):
    return item%2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

# print(list(map(multiply_by2, my_list)))
# print(list(filter(check_odd, my_list)))
# print(list(zip(my_list, your_list)))
print(reduce(accumulator, my_list, 0))

