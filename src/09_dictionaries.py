"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE

waypoints.append({
    "lat": 22,
    "lon": -1,
    "name": "a fourth place"
})



# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
waypoints[0].update({"lon": -130, "name": "not a real place"})

print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for i in waypoints:
    for k, e in i.items():
        print(e)
    

clear()
# This method removes all the elements from a dictionary.

# dictionary.clear()

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> car
# {'brand': 'Honda', 'model': 'CR-V', 'year': 2002}
# >>> car.clear()
# >>> car
# {}
# >>>

copy()
# This method returns a copy of the specified dictionary.

# dictionary.copy()

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> carbon_copy = car.copy()
# >>> carbon_copy
# {'brand': 'Honda', 'model': 'CR-V', 'year': 2002}
# >>> car
# {'brand': 'Honda', 'model': 'CR-V', 'year': 2002}
# >>>
fromkeys()
# This method returns a dictionary with the specified keys and values. The keys parameter is required, but the value parameter is optional. If we pass no value, the default value will be None.

# dict.fromkeys(keys, value)

# Example:

# Copy
# >>> x = ('key1', 'key2', 'key3')
# >>> y = 1
# >>> new_dict = dict.fromkeys(x, y)
# >>> new_dict
# {'key1': 1, 'key2': 1, 'key3': 1}
# >>> dict_without_values = dict.fromkeys(x)
# >>> dict_without_values
# {'key1': None, 'key2': None, 'key3': None}
# >>>
get()
# This method returns the value of the item with the specified key.

# dictionary.get(keyname, value)

# Keyname is required. The value parameter is optional, and this specifies the value to return if the specified key doesn’t exist. The default value to return if the key doesn’t exist is None.

# Example:

# Copy
# car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> x = car.get("model")
# >>> x
# 'CR-V'
# >>>
items()
# This method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

# The view object will reflect any future changes done to the dictionary.

# dictionary.items()

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> x = car.items()
# >>> x
# dict_items([('brand', 'Honda'), ('model', 'CR-V'), ('year', 2002)])
# >>>
keys()
# This method returns a view object. The view object contains the keys of the dictionary, as a list.

# The view object will reflect any future changes done to the dictionary.

# dictionary.keys

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> x = car.keys()
# >>> x
# dict_keys(['brand', 'model', 'year'])
# >>>
pop()
# This method removes the specified item from the dictionary. The value of the removed item is the return value of this method.

# dictionary.pop(keyname, defaultvalue)

# Keyname is a required parameter and specifies the keyname of the item you want to remove. The second parameter allows you to specify a value to return if the specified key doesn’t exit. If this value isn’t specified and no item with the specified key is found, it raises an error.

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> x = car.pop("model")
# >>> x
# 'CR-V'
# >>>
popitem()
# This method removes and returns some (key, value) pair as a tuple.

# dictionary.popitem(keyname, defaultvalue)

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> car.popitem()
# ('year', 2002)
# >>> car
# {'brand': 'Honda', 'model': 'CR-V'}
# >>> car["price"] = 4000
# >>> car
# {'brand': 'Honda', 'model': 'CR-V', 'price': 4000}
# >>> car.popitem()
# ('price', 4000)
# >>> car
# {'brand': 'Honda', 'model': 'CR-V'}
# >>>
setdefault()
# This method returns the value of the item with the specified key. If the key doesn’t exist, insert the key, with the specified value.

# dictionary.setdefault(keyname, value)

# The keyname parameter is required and specifies the keyname of the item you want to return the value from. The value parameter is optional. If the key exists, this parameter has no effect. If the key does not exist, this value becomes the key’s value.

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> x = car.setdefault("model", "Odyssey")
# >>> x
# 'CR-V'
# >>> y = car.setdefault("color", "black")
# >>> y
# 'black'
# >>> car
# {'brand': 'Honda', 'model': 'CR-V', 'year': 2002, 'color': 'black'}
# >>>
update()
# This method inserts the specified items to the dictionary. The specified items can be a dictionary, or an iterable object.

# dictionary.update(iterable)

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> car.update({"color": "black"})
# >>> car
# {'brand': 'Honda', 'model': 'CR-V', 'year': 2002, 'color': 'black'}
# >>>
values()
# This method returns a view object. The view object contains the values of the dictionary, as a list.

# The view object will reflect any future changes done to the dictionary.

# dictionary.values()

# Example:

# Copy
# >>> car = {
# ...     "brand": "Honda",
# ...     "model": "CR-V",
# ...     "year": 2002
# ... }
# >>> x = car.values()
# >>> x
# dict_values(['Honda', 'CR-V', 2002])
# >>> car["color"] = "black"
# >>> x
# dict_values(['Honda', 'CR-V', 2002, 'black'])
# >>>
