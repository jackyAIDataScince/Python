
def example():
    print('Hello, World!')
    print(100)
    print(5 + 5)
    #print() functions as newline character
    print('Hello, World!', end=' | ')
    print(100, end=' | ')
    print(5 + 5)

    name = 'Farhan'
    print('My name is ' + name)

    #face the following problem:
    name = 'Farhan'
    age = 27

    print('My name is '+ name + ' ')
    print('I am '+ age +'years old')

def example2():
    name = 'Farhan'
    age = 27

    print(f'My name is {name}')
    print(f'I am {age} years old')

    name = 'Farhan'

    print(name[0])
    print(name[1])
    print(name[2])
    print(name[3])
    print(name[4])
    print(name[5])

    name = 'Farhan'

    print(name[0:3])

def example3():
    name = 'Farhan'
    print(len(name))

    print('python is awesome'.capitalize())

    print('python is awesome'.upper())

    print('PYTHON IS AWESOME'.lower())

    print('PYTHON IS AWESOME'.islower())
    print('PYTHON IS AWESOME'.isupper())

    print('python is awesome'.replace('python', 'freeCodeCamp'))

    print('python is awesome'.split(' '))

    print(' '.join(['python', 'is', 'awesome']))

    a = 10
    b = 5

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

    a = 10
    b = 5

    print(a // b)

def example4():
    name = input('What is your name? ')
    print(f'Your name is {name}')

#def example5():
#    a = float(input('First: '))
#    b = float(input('Second: '))
#    op = input('Operation (sum/sub/mul/div): ')

#    if iop == 'sum':
#        print(f'a + b = {a + b}')
#    elif iop == 'sub':
#        print(f'a - b = {a - b}')
#    elif iop == 'mul':
#        print(f'a * b = {a * b}')
#    elif iop == 'div':
#        print(f'a / b = {a / b}')
#    else:
#        print('Invalid Operation!')

#def example6():
#    a = float(input('First: '))
#    b = float(input('Second: '))
#    iop = input('Operation (sum/sub/mul/div): ')

#    match iop:
#        case 'sum':
#            print(f'a + b = {a + b}')
#        case 'sub':
#            print(f'a - b = {a - b}')
#        case 'mul':
#            print(f'a * b = {a * b}')
#        case 'div':
#            print(f'a / b = {a / b}')
#        case _:
#            print('Invalid Operation!')

def example7():
    vowels = ['a', 'e', 'i', 'o', 'u']
    print(vowels)

    vowels = ['a', 'e', 'i', 'o', 'u']

    print(vowels[0])
    print(vowels[1])
    print(vowels[2])
    print(vowels[3])
    print(vowels[4])
    vowels = ['a', 'e']

    vowels.append('i')
    vowels.extend(['o', 'u'])

    print(vowels)


if __name__ == '__main__':
    example()
    example2()
    example3()
    example4()
    #example5()
    #example6()
    example7()

