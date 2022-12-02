with open('input.txt', 'r') as f:
    input_file = f.readlines()

total_calories = 0
elf_list = []

for line in input_file:
    if line != '\n':
        total_calories += int(line)
    else:
        elf_list.append(total_calories)
        print(f'{total_calories} Added to Elf List!')
        total_calories = 0

index = 0
current_calories = [0, 0, 0]

for elf in elf_list:
    index += 1

    elf_position = None

    for i, position in enumerate(current_calories):

        if elf > position:
            elf_position = i

    if elf_position is not None:
        if elf_position >= 2:
            current_calories[elf_position-2] = current_calories[elf_position-1]
        if elf_position >= 1:
            current_calories[elf_position-1] = current_calories[elf_position]
        current_calories[elf_position] = elf

print(current_calories)

total = 0

for place in current_calories:
    total += place

print(total)