from functools import reduce
my_pets = ['sisi', 'bibi', 'titi', 'carla'] #1 Capitalize all of the pet names and print the list
def capitalize(item):
    return item.upper()
print(list(map(capitalize, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e'] #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_numbers = [5,4,3,2,1]
print (list(zip(my_strings, my_numbers)))

scores = [73, 20, 65, 19, 76, 100, 88] #3 Filter the scores that pass over 50%
def check_over_50_percent(item):
    if item > 50:
        return item
print(list(filter(check_over_50_percent, scores)))

def combine_number(acc, num):
    return acc + num

print(reduce(combine_number,(my_numbers + scores)))
# def accumulator(acc, item):
#     return acc + item

# print(reduce(accumulator, (my_numbers + scores)))


