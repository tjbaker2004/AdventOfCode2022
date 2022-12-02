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
current_calories = 0

for elf in elf_list:
    index += 1

    if elf >= current_calories:
        current_calories = elf

print(f'{current_calories} is the correct answer!')
