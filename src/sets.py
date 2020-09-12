# add()
# This method adds an element to the set. If the element already exists in the set, it will not add the element.

# set.add(element)

# Example:

# Copy
# >>> fruits = {"apple", "banana", "cherry"}
# >>> fruits.add("orange")
# >>> fruits
# {'apple', 'orange', 'banana', 'cherry'}
# >>> fruits.add("banana")
# >>> fruits
# {'apple', 'orange', 'banana', 'cherry'}
# >>>
# clear()
# This method removes all elements in a set.

# set.clear()

# Example:

# Copy
# >>> fruits = {"apple", "banana", "cherry"}
# >>> fruits.clear()
# >>> fruits
# set()
# >>>
# copy()
# This method copies the set.

# set.copy()

# Example:

# Copy
# >>> fruits = {"apple", "banana", "cherry"}
# >>> x = fruits.copy()
# >>> x
# {'apple', 'banana', 'cherry'}
# >>>
# difference()
# This method returns a set that contains the difference between two sets. The returned set contains items that exist only in the first set, and not in both sets.

# set.difference(set)

# Example:

# Copy
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "apple"}
# >>> z = x.difference(y)
# >>> z
# {'banana', 'cherry'}
# >>> a = y.difference(x)
# >>> a
# {'google', 'microsoft'}
# >>>
# difference_update()
# This method removes the items that exist in both sets. It is different from the difference() method because that method returns a new set, without the unwanted items, and this method removes the unwanted items from the original set.

# set.difference_update(set)

# Example:

# Copy
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "apple"}
# >>> x.difference_update(y)
# >>> x
# {'banana', 'cherry'}
# >>>
# discard()
# This method removes the specified item from the set. It differs from the remove() method, because that method will raise an error if the specified item doesn’t exist, this method will not.

# set.discard(value)

# Example:

# Copy
# >>> fruits = {"apple", "banana", "cherry"}
# >>> fruits.discard("banana")
# >>> fruits
# {'apple', 'cherry'}
# >>> fruits.discard("orange")
# >>> fruits
# {'apple', 'cherry'}
# >>>
# intersection()
# This method returns a set that contains the similarity between two or more sets. The returned set contains only items that exist in both sets, or in all sets if the comparison is done with over two sets.

# set.intersection(set1, set2, ...)

# Example:

# Copy
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "apple"}
# >>> z = x.intersection(y)
# >>> z
# {'apple'}
# >>>
# >>> x = {"a", "b", "c"}
# >>> y = {"c", "d", "e"}
# >>> z = {"f", "g", "c"}
# >>> result = x.intersection(y, z)
# >>> result
# {'c'}
# >>>
# intersection_update()
# This method removes the items that are not present in both sets (or in all sets if the comparison is done between over two sets).

# set.intersection_update(set1, set2, ...)

# Example:

# Copy
# >>> x = {"a", "b", "c"}
# >>> y = {"c", "d", "e"}
# >>> z = {"f", "g", "c"}
# >>> x.intersection_update(y, z)
# >>> x
# {'c'}
# >>> y
# {'d', 'c', 'e'}
# >>> z
# {'f', 'c', 'g'}
# >>>
# isdisjoint()
# This method returns True if none of the items are present in both sets, otherwise it returns False.

# set.isdisjoint(set)

# Example:

# Copy
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "facebook"}
# >>> z = x.isdisjoint(y)
# >>> z
# True
# >>>
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "apple"}
# >>> z = x.isdisjoint(y)
# >>> z
# False
# >>>
# issubset()
# This method returns True if all items in the set exists in the specified set, otherwise it returns False.

# set.issubset(set)

# Example:

# Copy
# >>> x = {"a", "b", "c"}
# >>> y = {"f", "e", "d", "c", "b", "a"}
# >>> z = x.issubset(y)
# >>> z
# True
# >>> 
# >>> x = {"a", "b", "c"}
# >>> y = {"f", "e", "d", "c", "b"}
# >>> z = x.issubset(y)
# >>> z
# False
# >>>
# issuperset()
# This method returns True if all items in the specified set exists in the original set, otherwise it returns False.

# set.issuperset(set)

# Example:

# Copy
# >>> x = {"f", "e", "d", "c", "b", "a"}
# >>> y = {"a", "b", "c"}
# >>> z = x.issuperset(y)
# >>> z
# True
# >>> 
# >>> x = {"f", "e", "d", "c", "b"}
# >>> y = {"a", "b", "c"}
# >>> z = x.issuperset(y)
# >>> z
# False
# >>>
# pop()
# This method removes a random item from the set and returns the removed item.

# set.pop()

# Example:

# Copy
# >>> fruits = {"apple", "banana", "cherry"}
# >>> fruits.pop()
# 'apple'
# >>> fruits
# {'banana', 'cherry'}
# >>>
# remove()
# This method removes the specified element from the set. This method is different from the discard() method because remove() will raise an error if the specified item doesn’t exist, and the discard() method will not.

# set.remove(item)

# Example:

# Copy
# >>> fruits = {"apple", "banana", "cherry"}
# >>> fruits.remove("banana")
# >>> fruits
# {'apple', 'cherry'}
# >>>
# symmetric_difference()
# This method returns a set that contains all items from both sets, but not the items present in both sets. The returned set contains a mix of items that are not present in both sets.

# set.symmetric_difference(set)

# Example:

# Copy
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "apple"}
# >>> z = x.symmetric_difference(y)
# >>> z
# {'banana', 'cherry', 'microsoft', 'google'}
# >>>
# symmetric_difference_update()
# This method updates the original set by removing items that are present in both sets, and inserting the other items.

# set.symmetric_difference_update(set)

# Example:

# Copy
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "apple"}
# >>> x.symmetric_difference_update(y)
# >>> x
# {'banana', 'cherry', 'microsoft', 'google'}
# >>>
# union()
# This method returns a set that contains all items from the original set, and all items from the specified sets. You can specify as many sets as you want, separated by commas.

# set.union(set1, set2, ...)

# Example:

# Copy
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "apple"}
# >>> z = x.union(y)
# >>> z
# {'apple', 'microsoft', 'banana', 'cherry', 'google'}
# >>> 
# >>> x = {"a", "b", "c"}
# >>> y = {"f", "d", "a"}
# >>> z = {"c", "d", "e"}
# >>> result = x.union(y, z)
# >>> result
# {'b', 'f', 'd', 'a', 'c', 'e'}
# >>>
# update()
# This method updates the current set, by adding items from another set.

# set.update(set)

# Example:

# Copy
# >>> x = {"apple", "banana", "cherry"}
# >>> y = {"google", "microsoft", "apple"}
# >>> x.update(y)
# >>> x
# {'apple', 'microsoft', 'banana', 'cherry', 'google'}
# >>>