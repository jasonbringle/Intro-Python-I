# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x = x + y
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
del x[4]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    print(i * 1000)

# Lists
# Below, you will find some methods available on the list data structure.

# Methods
append()
# list.append(element)

# We use this method for appending and adding elements to a list. It is used to add elements to the last position of the list.

# Example:

# Copy
# >>> arr = ['math', 'biology', 1989, 2019]
# >>> arr.append(2021)
# >>> arr
# ['math', 'biology', 1989, 2019, 2021]
# >>>
insert()
# list.insert(position, element)

# This method inserts an element at a specified position.

# Example:

# Copy
# >>> arr = ['math', 'biology', 1989, 2019]
# >>> arr.insert(2, 2021)
# >>> arr
# ['math', 'biology', 2021, 1989, 2019]
# >>>
extend()
# list_one.extend(list_two)

# This method adds the contents of one list to the end of another list.

# Copy
# >>> arr_one = [1, 2, 3, 4, 5]
# >>> arr_two = [1, 2, 3]
# >>> arr_one.extend(arr_two)
# >>> arr_one
# [1, 2, 3, 4, 5, 1, 2, 3]
# >>>
sum()
# This method sums all the elements of a list.

# Example:

# Copy
# >>> arr = [1, 2, 3, 4, 5]
# >>> sum(arr)
# 15
# >>>
# Note: sum will only work if all the elements of the list are numbers.

count()
# This method calculates the total number of occurrences of an element of the list.

# list.count(element)

# Example:

# Copy
# >>> arr = [1, 1, 1, 2, 3]
# >>> arr.count(1)
# 3
# >>> arr.count(2)
# 1
# >>> arr.count(3)
# 1
# >>>
len()
# Note: This method works for any container type: list, dictionary, set, range, tuple, etc.

# This method calculates the total length of a list that we pass in as an argument.

# len(list)

# Example:

# Copy
# >>> arr = [1, 2, 3, 4, 5]
# >>> len(arr)
# 5
# >>>
index()
# This method returns the index of the first occurrence of the element passed in as an argument. You can also specify the start and end index where you want to conduct the search.

# Example:

# Copy
# >>> arr_two = ['a', 'b', 'c', 'd', 'e', 'a', 'b']
# >>> arr_two.index('a', 1)
# 5
# >>> arr_two.index('a', 1, 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 'a' is not in list
# >>>
min()
# Note: this method works on any iterable data structure.

# This method calculates the minimum of all the elements of the list.

# min(list)

# Example:

# Copy
# >>> arr = [4, 3, 2.5, 7, 0.7, 9]
# >>> min(arr)
# 0.7
# >>>
max()
# Note: this method works on any iterable data structure.

# This method calculates the maximum of all the elements of the list.

# max(list)

# Example:

# Copy
# >>> arr = [4, 3, 2.5, 7, 0.7, 9]
# >>> max(arr)
# 9
# >>>
sort()
# This method sorts the list in ascending order. You can set the reverse flag to True if you want to sort in descending order.

# list.sort(reverse_flag)

# Example:

# Copy
# >>> arr = [8, 4, 3, 9, 2, 1, 7, 6]
# >>> arr.sort()
# >>> arr
# [1, 2, 3, 4, 6, 7, 8, 9]
# >>> arr.sort(reverse=True)
# >>> arr
# [9, 8, 7, 6, 4, 3, 2, 1]
# >>>
reverse()
# This method reverses the order of elements in the list (without sorting).

# list.reverse()

# Example:

# Copy
# >>> arr = [8, 4, 3, 9, 2, 1, 7, 6]
# >>> arr.reverse()
# >>> arr
# [6, 7, 1, 2, 9, 3, 4, 8]
# >>>
pop()
# This method removes an element from the list. If we provide no index, it removes the last element. This method returns the removed element (which is different from del() which returns None).

# list.pop(index)

# Example:

# Copy
# >>> arr = [1, 2, 3, 4, 5]
# >>> arr.pop()
# 5
# >>> arr
# [1, 2, 3, 4]
# >>> arr.pop(1)
# 2
# >>> arr
# [1, 3, 4]
# >>>
del()
# This method deletes an element from the list at the index we pass in.

# del list[index]

# Example:

# Copy
# >>> arr = [1, 2, 3, 4, 5]
# >>> del arr[1]
# >>> arr
# [1, 3, 4, 5]
# >>>
remove()
# This method removes the element we pass in from the list.

# list.remove(element)

# Example:

# Copy
# >>> arr = ['a', 'b', 'c', 'd', 'e']
# >>> arr.remove('a')
# >>> arr
# ['b', 'c', 'd', 'e']
# >>>
