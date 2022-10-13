caption = 'Some text'
counter: int = 0

for letter in caption:
    counter = counter + 1
    # print(counter)
    print('\t' * counter + letter)

# IndexError: string index out of range
# print(caption[9])

print('******************')
print(caption[8])
print(caption[-1])
print(caption[len(caption) - 1])
print(caption[2])
print(caption[-2])
print(caption[1:4])
print(caption[:4])
print(caption[:4] + caption[5:])
print(caption[:4] * 4)

print('\t' * 4 + 'Marek')

