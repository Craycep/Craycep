# Simple Calculator
print('Simple Calculator App')

operation_choice = ['Add', 'Subtract', 'Multiply', 'Divide']

def add(x, y):
    """ Adds two numbers """
    return x + y


def subtract(x, y):
    """ Subtracts two numbers """
    return x - y


def multiply(x, y):
    """ Multiply two numbers """
    return x * y


def divide(x, y):
    """ Divide two numbers """
    return x / y


def check_if_user_has_finished():
    """
    Check that the user wants to finish or not.
    Performs some verification of the input.
    """
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish


def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu Options are:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('-' * 25)
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4'):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 4)')
    print('-' * 25)
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input('Input the first number: ')
    num2 = get_integer_input('Input the second number: ')
    return num1, num2


def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)


finished = False
while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1, n2 = get_numbers_from_user()
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result = multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)
    print('Operation choice: ', operation_choice[int(menu_choice) - 1])
    print('-_-' * 8)
    print('Result: ', result)
    print('=' * 15)
    finished = check_if_user_has_finished()

print('Bye!')
