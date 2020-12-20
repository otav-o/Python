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

- In Python a string is a sequence of characters contained within two quotes
  - You can also use single quotes
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



