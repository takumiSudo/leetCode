# Python Hashmaps (Dictionaries) Guide

## 1. Initialization
```python
my_dict = {}
```

## 2. Insert/Update
Add or update a key-value pair.
```python
my_dict['key'] = 'value'
```

## 3. Retrieve Value
Access the value associated with a given key.
```python
value = my_dict['key']
```
Or, safely get a value with a default if the key doesn't exist:
```python
value = my_dict.get('key', default_value)
```

## 4. Check Key Existence
Check if a key is in the dictionary.
```python
if 'key' in my_dict:
    print("Key exists!")
```

## 5. Increment Value
Add 1 to the value of a given key. If the key doesn't exist, initialize it with 1.
```python
my_dict['key'] = my_dict.get('key', 0) + 1
```

## 6. Delete Key-Value Pair
Remove a key-value pair from the dictionary.
```python
del my_dict['key']
```

## 7. Iterate Over Dictionary
Loop through all key-value pairs.
```python
for key, value in my_dict.items():
    print(key, value)
```

Remember, dictionary keys must be hashable. Common hashable types include integers, floats, strings, and tuples (if they contain only other hashable types).
