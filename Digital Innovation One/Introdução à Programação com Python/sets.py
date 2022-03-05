# Sets

numbers_set = {1, 2, 3, 4}  # there aren't duplicated elements
numbers_set.add(5)
print(numbers_set)

numbers_set.discard(2)
print(numbers_set)

numbers_set2 = {5, 5, 2, 3, 7, 6}

union_set = numbers_set.union(numbers_set2)


print('----\nFirst set: {}'.format(numbers_set))
print('Second set: {}'.format(numbers_set2))

print('----\nUnion: {}'.format(union_set))

intersection_set = numbers_set.intersection(numbers_set2)
print('Intersection: {}'.format(intersection_set))

values_in_first_set_that_are_not_in_second = numbers_set.difference(numbers_set2)
print('Difference: {}'.format(values_in_first_set_that_are_not_in_second))

values_in_first_set_that_are_not_in_second = numbers_set2.difference(numbers_set)
print('Difference 2: {}'.format(values_in_first_set_that_are_not_in_second))

symmetric_difference = numbers_set.symmetric_difference(numbers_set2)  # union, removing common values
print('Symmetric difference {}'.format(symmetric_difference))

print(type({1}))
# union(), difference(), intersection(),

# -------

# subset
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))  # True

# superset
print(set_b.issuperset(set_a))  # True

# convert list to set (for example, when you want to remove duplicated entries)
colors_list = ['yellow', 'purple', 'red', 'pink', 'pink', 'yellow', 'blue']
colors_set = set(colors_list)
print(colors_list, colors_set)

# set to list
colors_list = list(colors_set)
print(colors_list)
