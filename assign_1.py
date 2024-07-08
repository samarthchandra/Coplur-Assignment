array = [1, 2, 3, 4, 5]

try:
    index = int(input('Enter an index to retrieve from the list: '))
    value = array[index]
    print(f'The value at index {index} is: {value}')

except IndexError:
    print('Error: Index out of range.')

except ValueError:
    print('Error: Please enter a valid integer.')

finally:
    print('Execution completed.')