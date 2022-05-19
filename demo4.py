# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    vowels = ['a', 'i', 'o', 'u']

    vowels.insert(1, 'e')

    print(vowels)

    vowels = ['a', 'e', 'i', 'o', 'u']

    popped_item = vowels.pop()

    print(popped_item)
    print(vowels)

    vowels = ['a', 'e', 'i', 'o', 'u']

    vowels.remove('e')

    print(vowels)

    vowels = ['u', 'e', 'a', 'o', 'i']

    vowels.reverse()

    print(vowels)

    vowels = ('a', 'e', 'i', 'o', 'u')

    print(vowels)

    #Loop in Python
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in vowels:
        print(letter.upper())

    #Dictionaries
    sentence = 'the quick brown fox jumped over the lazy dog'

    record = {}

    for letter in sentence:
        if letter in record:
            record[letter] += 1
        else:
            record[letter] = 1

    print(record)

    def sum(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    a = float(input('First: '))
    b = float(input('Second: '))
    op = input('Operation (sum/sub/mul/div): ')

    if op == 'sum':
        print(f'a + b = {sum(a, b)}')
    elif op == 'sub':
        print(f'a - b = {sub(a, b)}')
    elif op == 'mul':
        print(f'a * b = {mul(a, b)}')
    elif op == 'div':
        print(f'a / b = {div(a, b)}')
    else:
        print('Invalid Operation!')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
