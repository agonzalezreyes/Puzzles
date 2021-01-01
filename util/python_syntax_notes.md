# Python syntax notes

## Table of contents
1. [args and kwargs](#first)
2. [String Indexing and Slicing](#second)
3. [Loops](#third)
4. [Exception Handling](#fourth)
5. [in and not](#fifth)
6. [Multiple assignments](#sixth)
7. [Augmented Assignment Operators](#seventh)
8. [Lists](#eighth)
9. [Tuples](#ninth)
10. [Dictionaries](#tenth)
11. [Sets](#eleventh)
12. [Comprehensions](#twelfth)
13. [Regular Expressions](#thirteenth)
14. [Lambda Functions](#fourteenth)

---
### args and kwargs <a name="first"></a>
- In a function declaration `*` means put the rest of the positional arguments into a tuple named  `<name> `, while  `**` is the same for keyword arguments but with a dictionary. 
- In a function call `*` means unpacking the tuple or list named `<name>` to positional arguments at this position, while `**` is the same for keyword arguments.
For instance:
```python
# here, args is a tuple (of the positional arguments except the first since it is specified as callback), while kwargs is a dictionary.
def advance(callback, *args, **kwargs):
    # we unpack them so they become normal arguments to callback()
    return callback(*args, **kwargs)
```

For example, `*args` for indefinite amount of positional arguments:
```python
>>> def frutas(*args):
>>>    for f in args:
>>>       print(f)

>>> frutas("manzana", "platano", "uvas")

"manzana"
"platano"
"uvas"
```
For example, `**kwargs` for indefinite number of keyword arguments:
```python
>>> def frutas(**kwargs):
>>>    for key, value in kwargs.items():
>>>        print("{0}: {1}".format(key, value))

>>> frutas(nombre = "manzana", color = "roja")
nombre: manzana
color: roja
```
---
### String Indexing and Slicing <a name="second"></a>
Replace character at `position` in string:
```python
string = string[:position] + character + string[position+1:]
```
Indexing
```python
>>> title = 'Hello world!'
>>> title[0]
'H'
>>> title[2]
'l'
>>> title[-1]
'!'

# slicing
>>> title[0:5]
'Hello'
>>> title[6:]
'world!'
>>> title[6:-1]
'world'
>>> title[:-1]
'Hello world'
>>> title[::-1]
'!dlrow olleH'
```
Other string methods:
`isalpha()`: checks if the string consists only of letters and is not blank.
`isalnum()`: checks if the string consists only of letters and numbers and is not blank.
`isdecimal()`: checks if  the string consists only of numeric characters and is not blank.
`isspace()`: checks if the string consists only of spaces,tabs, and new-lines and is not blank.
`istitle()`: checks if string consists only of words that begin with an uppercase letter followed by only lowercase letters.

`startswith()` and `endswith()`:
```python
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'Hello world!'.startswith('123')
False
```

`join()` and `split()`:
```python
>>> ', '.join(['a', 'b', 'c'])
'a, b, c'

>>> ' '.join(['I', 'am', 'Alex'])
'I am Alex'

>>> 'BBB'.join(['I', 'am', 'Alex'])
'IBBBamBBBAlex'

>>> 'I am Alex'.split()
['I', 'am', 'Alex']

>>> 'IBBBamBBBAlex'.split('BBB')
['I', 'am', 'Alex']
```

`strip()`, `rstrip()`, and `lstrip()`:
```python
>>> greeting = '    Hello World     '
>>> greeting.strip()
'Hello World'

>>> greeting.lstrip()
'Hello World    '

>>> greeting.rstrip()
'    Hello World'
```
---
### Loops <a name="third"></a>
```python
>>> for i in range(start=0, stop=10, step=2):
>>>    print(i)
0
2
4
6
8
```
```python
>>> for i in range(start=0, stop=10, step=2):
>>>    print(i)
0
2
4
6
8
```
```python
>>> for i in range(start=5, stop=-1, step=-1):
>>>     print(i)
5
4
3
2
1
0
```
while-loop:
```python
abc = ["a", "b", "c", "d"]
i = 0
while i < len(colors):
    print(colors[i])
    i += 1
```
`range()` of `len()` 
```python
abc = ["a", "b", "c", "d"]
for i in range(len(colors)):
    print(colors[i])
    
prez = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for i in range(len(prez)):
    print("President {}: {}".format(i + 1, presidents[i]))
```
for-in:
```python
abc = ["a", "b", "c", "d"]
for color in colors:
    print(color)
```
`enumerate()` : get both the index and the value of each item.
```python
prez = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))
```
Looping multiple lists and `zip()`:
```python
chroma = ["red", "green", "blue"]
ratios = [0.2, 0.3, 0.1]
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))

# with zip()
for color, ratio in zip(chroma, ratios):
    print("{}% {}".format(ratio * 100, color))
```
---
### Exception Handling <a name="fourth"></a>
The `finally` section will always be executed, whetheer the expection was raised or not:
```python
def spam(divideBy):
>>>     try:
>>>         return 42 / divideBy
>>>     except ZeroDivisionError as e:
>>>         print('Error: Invalid argument: {}'.format(e))
>>>     finally:
>>>         print("-- division finished --")
```
---
### in and not <a name="fifth"></a>
```python
>>> 'hola' in ['hello', 'hi', 'hola']
True
>>> greet = ['hello', 'hi', 'hola']
>>> 'bye' in greet
False
>>> 'hola' not in greet
False
>>> 'bye' not in greet
True
```
With Dictionaries
```python
doggo = {'name': 'Spunky', 'age': 0.2}

>>> 'name' in doggo.keys()
True

>>> 'Spunky' in doggo.values()
True

# omitting keys() when checking a key
>>> 'color' in doggo
False
>>> 'color' not in doggo
True
```
---
### Multiple assignments <a name="sixth"></a>
Instead of this:
```python
>>> characteristics = ['yuge', 'green']
>>> size = characteristics[0]
>>> color = characteristics[1]
```
... this can be done as:
```python
>>> characteristics = ['yuge', 'green']
>>> size, color = characteristics
```
Swaping values:
```python
>>> a, b = 'AAA', 'BBB'
>>> a, b = b, a
>>> print(a)
'BBB'
>>> print(b)
'AAA'
```
---
### Augmented Assignment Operators <a name="seventh"></a>
```python
>>> s = 'Hello'
>>> s += ' world!'
>>> print(s)
'Hello world!'

>>> z = ['Zoo']
>>> z *= 3
>>> print(z)
['Zoo', 'Zoo', 'Zoo']
```
---
### Lists <a name="eighth"></a>
Slicing lists
```python
>>> A = ['a', 'b', 'c', 'd']
>>> A[0:4]
['a', 'b', 'c', 'd']
>>> A[1:3]
['b', 'c']
>>> A[0:-1]
['a', 'b', 'c']
>>> A[:2]
['a', 'b']
>>> A[1:]
['b', 'c', 'd']
```

Copy with slicing:
```python
>>> A2 = A[:]
['a', 'b', 'c', 'd']
>>> A.append('e')
>>> A
['a', 'b', 'c', 'd', 'e']
>>> A2
['a', 'b', 'c', 'd']
```

Negative Indexing
```python
>>> spam = ['a', 'b', 'c', 'd']
>>> spam[-1]
'd'
>>> spam[-3]
'b'
```

Getting Index from List Item:
```python
>>> spam = ['A', 'B', 'C', 'D']
>>> spam.index('B')
1
```

`append()` and `insert()`
```python
>>> A = ['cat', 'dog']
>>> A.append('mouse')
>>> print(A)
['cat', 'dog', 'mouse']
```
```python
>>> A = ['cat', 'dog']
>>> A.insert(1, 'mouse')
>>> print(A)
['cat', 'mouse', 'dog']
```

`remove()`
```python
>>> A = ['cat', 'dog']
>>> A.remove('cat')
>>> A
['dog']
```

`sort()`
```python
>>> A = [2, 5, 3.14, 1, -7]
>>> A.sort()
>>> print(A)
[-7, 1, 2, 3.14, 5]

>>> B = ['dogs', 'ants', 'cats']
>>> B.sort()
>>> print(B)
['ants', 'cats', 'dogs']

# reverse order sort
>>> B.sort(reverse=True)
>>> print(B)
['dogs', 'cats', 'ants']

# regular alphabetical order
>>> abc = ['a', 'z', 'A', 'Z']
>>> abc.sort(key=str.lower)
>>> print(abc)
['a', 'A', 'z', 'Z']
```

`sorted()` gives a new list
```python
>>> l = ['a', 'b', 'c']
>>> l2 = sorted(l)
>>> print(l2)
['a', 'b', 'c']
```
---
### Tuples <a name="ninth"></a>
```python
>>> trio = ('hola', 10, 'adios')
>>> print(trio[0])
>>> 'hola'

>>> trio[1:3]
(10, 'adios')

>>> len(trio)
3
```
`list()` <--> `tuple()`
```python
>>> tuple(['hola', 10, 'adios'])
('hola', 10, 'adios')

>>> list(('hola', 10, 'adios'))
['hola', 10, 'adios']

>>> list('hola')
['h', 'o', 'l', 'a']
```
---
### Dictionaries <a name="tenth"></a>
```python
myDoggo = {'name': 'Speedy Gonzalez', 'size': 'fit', 'color': 'tri', 'age': 3}

# values()
>>> for i in myDoggo.values():
>>>     print(i)
Speedy Gonzalez
fit
tri
3

# keys()
>>> for k in myDoggo.keys():
>>>     print(k)
name
size
color
age

# items()
>>> for i in myDoggo.items():
>>>     print(i)
('name', 'Speedy Gonzalez')
('size', 'fit')
('color', 'tri')
('age', 3)

>>> doggo = {'color': 'tri', 'age': 3}
>>>
>>> for k, v in spam.items():
>>>     print('Key: {} Value: {}'.format(k, str(v)))
Key: age Value: 3
Key: color Value: tri
```

`setdefault()`
Instead of this:
```python
doggo = {'name': 'Spunky', 'age': 0.2}

if 'color' not in spam:
    doggo['color'] = 'tri'
```
... do this:
```python
>>> doggo = {'name': 'Spunky', 'age': 0.2}
>>> spam.setdefault('color', 'tri')
'tri'
>>> print(doggo)
{'color': 'tri', 'name': 'Spunky', 'age': 0.2}
```
---
### Sets <a name="eleventh"></a> 
Can be done in two ways:
```python
>>> s2 = set([1, 2, 3])
# AND
>>> s1 = {1, 2, 3} # except when creating an empty set--you will get an empty dictonary

>>> s1 = {}
>>> type(s)
<class 'dict'>

# unordered data type, removes duplicates
>>> s = {1, 2, 3, 2, 3, 4}
>>> s
{1, 2, 3, 4}

# cannot be indexed
>>> s = {1, 2, 3}
>>> s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>>

# add()
>>> s = {1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}

# update()
>>> s = {1, 2, 3}
>>> s.update([2, 3, 4, 5, 6])
>>> s
{1, 2, 3, 4, 5, 6} 
```

set `remove()` and `discard()`: Both do the same operation but `remove()` will raise a `key error`
```python
>>> s = {1, 2, 3}
>>> s.remove(3)
>>> s
{1, 2}
>>> s.remove(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
```
```python
>>> s = {1, 2, 3}
>>> s.discard(3)
>>> s
{1, 2}
>>> s.discard(3)
>>>
```
`clear()`: clear contents of the set

`union()` or `|`
```python
>>> s1 = {1, 2, 3}
>>> s2 = {3, 4, 5}
>>> s1.union(s2)  # or 's1 | s2'
{1, 2, 3, 4, 5}
```
`intersection()` or `&`
```python
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s3 = {3, 4, 5}
>>> s1.intersection(s2, s3)  # or 's1 & s2 & s3'
{3}
```
`difference()` or `-`
```python
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s1.difference(s2)  # or 's1 - s2'
{1}
>>> s2.difference(s1) # or 's2 - s1'
{4}
```
`symetric_difference()` or `^`
```python
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s1.symmetric_difference(s2)  # or 's1 ^ s2'
{1, 4}
```
---
### Comprehensions <a name="twelfth"></a> 
```python
# list
>>> a = [1, 3, 6]
>>> a2 = [i - 1 for i in a]
>>> print(a2)
[0, 2, 5]

# set
>>> a = {"aaa", "bbb"}
>>> {s.upper() for s in a}
{"AAA", "BBB"}

# dict
>>> a = {'name': 'Speedy', 'age': 3}
>>> {v: k for k, v in c.items()}
{'Speedy': 'name', 3: 'age'}
```
---
### Regular Expressions with `import re` <a name="thirteenth"></a> 
```python
>>> phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

>>> res = phone_regex.search('Phone is 111-222-4444')

>>> print('Number found: {}'.format(res.group()))
Phone number found: 111-222-4444

# group() with parentheses 
>>> phone_regex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

>>> res = phone_regex2.search('Phone is 111-222-4444')

>>> res.group(1)
'111'
>>> res.group(2)
'222-4444'
>>> res.group(0)
'111-222-4444'
>>> mo.group()
'111-222-4444'

>>> res.groups()
('111', '222-4444')
>>> area_code, main_number = res.groups()
>>> print(area_code)
111
>>> print(main_number)
222-4444

>>> phone_regex3 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
>>> phone_regex3.findall('Cell: 111-222-4444 Work: 222-333-5555')
['111-222-4444', '222-333-5555']
```
---
###  Lambda Functions <a name="fourteenth"></a> 
Consider the following:
```python
>>> def add(x, y):
        return x + y

>>> add(2, 3)
5
```
... equivalently:
```python
>>> add = lambda x, y: x + y
>>> add(2, 3)
5

>>> (lambda x, y: x + y)(2, 3)
5
```
Lambda functions as lexical closures:
```python
>>> def make_addition(n):
        return lambda x: x + n

>>> add_2 = make_addition(2)
>>> add_4 = make_addition(4)

>>> add_2(4)
6
>>> add_4(4)
8
```
