##################################################
'''
Q1: 
'''

# TODO: Write your code here
list = ["It", "was", "a", "stormy", "night"]

print(list)
##################################################
'''
Q2:
'''

# TODO: Write your code here
list.insert(3, "dark")
list.insert(4, "and")

print(list)
##################################################
'''
Q3:
'''

# TODO: Write your code here
list[1] = "IS"

print(list)
##################################################
'''
Q4:
'''

# TODO: Write your code here
removal = []
for word in list:
    if "a" in word:
        removal.append(word)

for word in removal:
    list.remove(word)

print(list)
##################################################
'''
Q5:
'''

# TODO: Write your code here
num_list = []
for i in range(10):
    num_list.append(i*2)
print(num_list)
##################################################
'''
Q6:
'''

# TODO: Write your code here


def fill(list, new_num):
    result = []
    for num in list:
        result.append(new_num)
    return result


my_list = [42, -7, 3, 0, 15]
my_list = fill(my_list, 2)

print(my_list)
##################################################
