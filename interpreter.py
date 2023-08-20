accumulator = 0

file_loc = input('File path: ')
ascii_out = input('ASCII(T or F): ')

if ascii_out.upper() == 'T':
    ascii_out = True
else:
    ascii_out = False

if file_loc[(len(file_loc)-3):(len(file_loc))] == '.df':
    pass
else:
    file_loc = file_loc + '.df'

with open(file_loc, 'r') as file:
    contents = file.read()
    for instruction in contents:
        if (accumulator == -1) or (accumulator == 256):
            accumulator = 0

        if instruction not in ['i', 'o', 'd', 's']:
            continue
        else:
            match instruction:
                case 'i':
                    accumulator += 1
                case 'o':
                    if ascii_out:
                        print(chr(accumulator), end='')
                    else:
                        print(accumulator)
                case 'd':
                    accumulator = accumulator - 1
                case 's':
                    accumulator = accumulator**2
