from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

Current_file = open(input_file)

print('First let\'s print the whole file:\n')

print_all(Current_file)

print('Now let\'s rewind, kind of like a tape.')

rewind(Current_file)

print('let\'s print three lines:')

Current_line = 1
print_a_line(Current_line, Current_file)

Current_line += 1
print_a_line(Current_line, Current_file)

Current_line += 1
print_a_line(Current_line, Current_file)
