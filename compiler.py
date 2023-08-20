from os import mkdir

file_loc = input('File path: ')
output_name = input('Output name: ')
ascii_out = input('ASCII(T or F): ')

if ascii_out.upper() == 'T':
    ascii_out = True
else:
    ascii_out = False

accumulator = 0

if file_loc[(len(file_loc)-3):(len(file_loc))] == '.df':
    pass
else:
    file_loc = file_loc + '.df'

try:
    mkdir('./bin')
except FileExistsError:
    pass

bin = open(f'./bin/{output_name}.py', 'w')
bin.write('a=0;')
bin.close()

with open(file_loc, 'r') as file, open(f'./bin/{output_name}.py', 'a', encoding='utf-8') as binary:
    contents = file.read()
    for instruction in contents:
        # print(instruction)

        if instruction not in ['i', 'o', 'd', 's']:
            continue
        else:
            match instruction:
                case 'i':
                    accumulator += 1
                    binary.write('a+=1;')
                case 'o':
                    # print(accumulator)
                    if ascii_out:
                        binary.write('print(chr(a),end="");')
                    else:
                        binary.write('print(a);')
                case 'd':
                    accumulator = accumulator - 1
                    binary.write('a=a-1;')
                case 's':
                    accumulator = accumulator**2
                    binary.write('a=a**2;')

            if (accumulator == -1) or (accumulator == 256):
                accumulator = 0
                binary.write('a=0;')
    binary.close()
