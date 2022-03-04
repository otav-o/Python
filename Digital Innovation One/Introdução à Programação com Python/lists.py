list_a = [1, 2, 3, 'hi']  # a list can store different types
numbers_list = [1, 9, 3, 7, 12, 3.5, 2]  # a list can store different types
animals_list = ['dog', 'cat', 'elephant']

print(type(list_a))

for x in animals_list:
    print(x)

print('Sum: {}'.format(sum(numbers_list)))
print('Max: {}'.format(max(numbers_list)))
print('Min: {}'.format(min(numbers_list)))

print('Max: {}'.format(max(animals_list)))  # last word in alphabetical order
print('Min: {}'.format(min(animals_list)))  # first word

if 'cat' in animals_list:
    print('There is a cat in the list')

new_list = animals_list * 3
print(new_list, len(new_list))

animals_list.append('wolf')
new_list.pop(0)  # removes a specific index
new_list.pop()  # removes last index
new_list.remove('elephant')  # removes value first occurrence

print(new_list, len(new_list))

new_list.sort()  # alphabetical or numerical order
print(new_list)

new_list.reverse()
print(new_list)
