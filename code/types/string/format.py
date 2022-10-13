caption = '%s, jest %s' % ('Lorem ipsum', 'Przykładowym tekstem')
print(caption)

caption = '{0}, jest {1}'.format('Lorem ipsum', 'Przykładowym tekstem')
print(caption)

# Wartości liczbowe są opcjonalne.
caption = '{}, jest {}'.format('Lorem ipsum', 'Przykładowym tekstem')
print(caption)

numberString = '{: 25.3f}'.format(296999.2567)
print(numberString)

numberString = '%19.2f | %+05d' % (3.14159, -42)
print(numberString)

print(dir(caption))
print(help(caption.index))
print(help(caption.join))
print(help(caption.index))



