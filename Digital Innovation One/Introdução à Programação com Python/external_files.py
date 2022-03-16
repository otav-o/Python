# file = open('text.txt', 'w')  # overrides/recreates all content
file = open('text.txt', 'a')  # create if not exists

file.write('First content\n')
file.write('Second content\n')
# file.close()


file.write('First content\n')
file.write('Second content')
file.close()


def write_file(path, text):
    file = open(path, 'w')
    file.write(text)
    file.close()


def update_file(path, text):
    file = open(path, 'a')
    file.write(text)
    file.close()


def read_file(path):
    file = open(path, 'r')
    content = file.read()
    return content


def grades_average(file_path):
    file = open(file_path, 'r')
    students = file.read()
    students = students.split('\n')  # creates a list
    print(students)
    for x in students:
        print(x)
        grades_list = x.split(',')
        student = grades_list[0]
        grades_list.pop(0)
        print(student)
        print(grades_list)
        # average = lambda grades: sum((int(i) for i in grades)) / len(grades)
        # print(average(grades_list))


def copy_file(name):
    import shutil
    shutil.copy(name, '~/Desktop')
    # shutil.move(name, '~/Desktop/new_name')


if __name__ == '__main__':
    print(read_file('text.txt'))
    student = 'Helen, 5, 6, 2, 6\n'
    write_file('grades.txt', student)

    content = open('grades.txt', 'r').read()
    print(content)

    grades_average('grades.txt')

    copy_file('grades.txt')
