## About the course

- 3h to complete, started Sunday, 20/12/2020

> Jupyter Notebooks are a popular data science tool that lets Data Scientists write code, see the results, and describe what's happening -- all in a single document.

## Types in Python

- You can use `type()` function to receive the data type of parameter

```python
type(11) # int
type(21.213) # float
type("Hello Python") # str
```

- Typecasting

```python
float(2) # 2.0
int(1.1) # 1
int('1') # 1
int('A') # error

str(1) # "1"
str(4.5) # '4.5'

int(True) # 1
int(False) # 0

bool(1) # True
bool(0) # False
```

- In Python, if you cast a float to an integer, the conversion truncates towards zero.
- Boolean: True and False (with capital letter)
- If you cast a boolean True to integer, you will get 1
- Do casting functions return the type or print on screen?
- Differences between syntactic vs semantic error

## Expressions and Variables

Operands (numbers) operators (math signals)

`+ - / * //`

- Double slash (`//`) for integer division, where the result is rounded

```python
my_variable = 10
```

## String Operations

- In Python a string is a sequence of characters contained within two or single quotes
- Think of a string as an ordered sequence. Each element in the sequence can be accessed using an index represented by the array of numbers

```python
name = "Michael Jackson"
name[0] # M
name[6] # l
name[-1] # n
name[-15] # M
```

- You can also use negative indexing with strings
- The first last element is given by the index -1, and so on

```python
name[::2] # "McalJcsn"; select every second variable
name[0:5:2] # "Mca"; select second variable from 0 to 5
name[0:5] # Micha; 0 to 4 (excludes 5)
```

```python
len("Michael Jackson") # 15
statement = name + " is the best" # concatenation
```

```python
3 * "Michael Jackson " # replicating string
```

- **Strings are immutable**: you cannot change its value, but you can create a new string (and set it to the original variable)

```python
name[0] = "J" # Error
```

### Scape sequences

- `\n` represents a new line
- `\t` gives a tab 
- If you want to place a backlash in your string, use a double backslash (and the result will be just one).

### String methods

- When we apply a method to the string "A" we get a new string "B" that is different from "A"

```python
B = A.upper()
B = A.replace('Michael', 'Janet') - replaces a segment of the string
name.find('el') # 5
# if the substring is not in the string, the output is negative one (-1)
```

| Syntax                                    | What it does                                                 |
| ----------------------------------------- | ------------------------------------------------------------ |
| `str2 = str1.upper()`                     | Set all characters to uppercase                              |
| `str2 = str1.replace('Michael', 'Janet')` | Replaces a segment of the string (first argument) with the second argument |
| `str.find('el')`                          | Returns the start position of substring                      |

```python
Letters="ABCDEFGHIJK"
Letters[0:4] # ABCD, 0-3 (indexes)

Good="GsoAo+d"
Good[::2]
```

---

> Module 2 - Python Data Structures

### Tuples

- Compound data type
- Tuples are an ordered sequence
- Tuples are written as comma-separated elements within parentheses

```python
Ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
tuple1 = ('bom dia', 10, 1.5, True)

type(tuple1) # tuple
```

- Several types can be contained in a tuple, but the type of the variable is "tuple"
- Indexes are used to access each element
  - -1 is the last element, and -2 penultimate, etc.
- **Concatenating tuples**

```python
tuple2 = tuple1 + ("boa tarde", 10)
# ("bom dia", 10, 1.5, True, "boa tarde", 10)
```

- **Tuple slicing**
  - the last index is one larger than the index you want
  - but the first enters the selected slice

```python
tuple2[0:3] # ('bom dia', 10, 1.5)
tuple2[3:6] # (True, 'boa tarde', 10)
```

- Length of a tuple: `len()`

```python
len(("bom dia", 10, 1.5, True, "boa tarde", 10)) # 6
```

- **Tuples are immutable** and if we would like to manipulate one we must create a new tuple instead.
- Two variables can reference the same tuple object

```python
tuple1 = tuple2 # there is only one tuple, no copy
tuple2[0] = "New element!"; # error!

tupleSorted = sorted(tuple); # creates a new tuple
```

- **Nesting**: a tuple can contain other tuples as well as other complex data types
  - Add more square brackets to access deep tuples elements or string characters, for example.

```python
bigTuple = (1, 2.5, ('hi', (5,4)), (10, 21.2))

bigTuple[0] # 1
bigTuple[2] # ('hi', (5,4)) 
bigTuple[2][0] # 'hi'
bigTuple[2][0][1] # 'i'
```

### Lists

- Are also ordered sequences
- A List is represented with square brackets `[]`
- **Lists are mutable**

```python
list1 = ['Michael Jackson', 10.1, 1982, [1,2], ('A', 1)]
```

- Index works same as tuples, including negative numbers, slicing and concatenating.

```python
list1.extend(['pop', 10]) # this method adds these list elements to the list1 (concatenation)
# the original list is modified!

# it is also concatenation:
list1 = list1 + list2
```

- Adding a new element, modifying elements, deleting

```python
list1.append(new element) # adds to list end (creating the next index)
list1[0] = "hard rock"
del(list1[0]) # replaces indexex
```

- Split a string in elements of a list

```python
"hard rock".split(",") # default separator is space
```

- Lists are objects
  - If a and b references the same list (aliasing), changes occur to both variables
  - `b = a[:]` clone a list (so there will be two objects and changes won't occur simultaneously)
- `print(list1)` - prints all elements (you don't need a `foreach`) - also works with tuples

```python
B=["a","b","c"]
B[0] = B[0].upper()
print(B)
```

```python
C_tuple=(-5, 1, -3)
sortedList = list(C_tuple)
print(sorted(sortedList)) # [-5, -3, 1]
```

> `help()` function can be useful. help(list1)
>
> tuple1.index("disco")

### Sets

