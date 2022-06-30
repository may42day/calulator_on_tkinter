import numbers
from tkinter import *
# from tkinter import ttk

# Functions
def insert_number(value):
    current_number = result_of_operation.get()
    if value == 0 and current_number == '0' or value == ',' and ',' in current_number:
        pass
    elif value == ',':
        if len(current_number) == 0:
            result_of_operation.set('0,')
        else:
            result_of_operation.set(current_number + ',')
    else:
        result_of_operation.set(current_number + str(value))


def correct_number_value(number):
    if len(number) == 0:
        pass
    else:
        if ',' in number or '.' in number:
            number = float(number.replace(',', '.'))
            if str(number)[-1] == '0':
                return int(str(number)[:-2])
            else:
                return float(number)
        else:
            return int(number) 


def change_sign():
    current_number = result_of_operation.get()
    if len(current_number) == 0:
        pass
    elif '-' in current_number[0] :
        result_of_operation.set(current_number[1:])
    else:
        result_of_operation.set('-' + current_number)

saved_number = 0
sign_of_previous_operation = ''

def do_previous_opperation(sign):
    global sign_of_previous_operation

    if len(result_of_operation.get()) == 0:
        # sign_of_previous_operation = sign
        # print(output_of_last_operation_variable.get()[:-3])
        # new_output = f'{output_of_last_operation_variable.get()[:-3]} {sign}'
        # print(output_of_last_operation_variable.get()[:-3])
        # print(new_output)
        # output_of_last_operation_variable.set(new_output)
        # return
        pass
    else:
        current_number = correct_number_value(result_of_operation.get())
        if sign == '+':
            result = saved_number + current_number
        elif sign == '-':
            result = saved_number - current_number
        elif sign == '/':
            result = saved_number / current_number
        elif sign == '*':
            result = saved_number * current_number
        result_of_operation.set(str(result).replace('.', ','))

def operation_to_add():
    global sign_of_previous_operation
    global saved_number

    if len(sign_of_previous_operation) == 0:
        sign_of_previous_operation = '+'
        saved_number = correct_number_value(result_of_operation.get())
        output_of_last_operation_variable.set(f'{saved_number} + ')
        result_of_operation.set('')
    else:
        do_previous_opperation(sign_of_previous_operation)
        sign_of_previous_operation = '+'
        output_of_last_operation_variable.set(f'{result_of_operation.get()} + ')
        saved_number = correct_number_value(result_of_operation.get())
        result_of_operation.set('')

def operation_to_minus():
    global sign_of_previous_operation
    global saved_number

    if len(sign_of_previous_operation) == 0:
        sign_of_previous_operation = '-'
        saved_number = correct_number_value(result_of_operation.get())
        output_of_last_operation_variable.set(f'{saved_number} - ')
        result_of_operation.set('')
    else:
        do_previous_opperation(sign_of_previous_operation)
        sign_of_previous_operation = '-'
        output_of_last_operation_variable.set(f'{result_of_operation.get()} - ')
        saved_number = correct_number_value(result_of_operation.get())
        result_of_operation.set('')

def operation_to_divide():
    global sign_of_previous_operation
    global saved_number

    if len(sign_of_previous_operation) == 0:
        sign_of_previous_operation = '/'
        saved_number = correct_number_value(result_of_operation.get())
        output_of_last_operation_variable.set(f'{saved_number} / ')
        result_of_operation.set('')
    else:
        do_previous_opperation(sign_of_previous_operation)
        sign_of_previous_operation = '/'
        output_of_last_operation_variable.set(f'{result_of_operation.get()} - ')
        saved_number = correct_number_value(result_of_operation.get())
        result_of_operation.set('')

def operation_to_multiply():
    global sign_of_previous_operation
    global saved_number

    if len(sign_of_previous_operation) == 0:
        sign_of_previous_operation = '*'
        saved_number = correct_number_value(result_of_operation.get())
        output_of_last_operation_variable.set(f'{saved_number} * ')
        result_of_operation.set('')
    else:
        do_previous_opperation(sign_of_previous_operation)
        sign_of_previous_operation = '*'
        output_of_last_operation_variable.set(f'{result_of_operation.get()} - ')
        saved_number = correct_number_value(result_of_operation.get())
        result_of_operation.set('')

def operation_to_square():
    current_number = correct_number_value(result_of_operation.get())
    output_of_last_operation_variable.set(f'sqr({current_number})')
    result = str(current_number ** 2).replace('.', ',')
    result_of_operation.set(result)

def operation_to_square_root():
    current_number = correct_number_value(result_of_operation.get())
    output_of_last_operation_variable.set(f'sqrt({current_number})')
    result = str(current_number ** 0.5).replace('.', ',')
    if result[-1] == '0':
        result_of_operation.set(result[:-2])
    else:
        result_of_operation.set(result)

def operation_to_equal():
    pass

def operation_to_clear():
    result_of_operation.set('0')
    output_of_last_operation_variable.set('')


# TTK module
root = Tk()
root.title("Calculator")
root.geometry('300x450+100+100')


# Creating mainframe
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creating label with output of last operation
output_of_last_operation_variable = StringVar()
output_of_last_operation_label = Label(mainframe, width = 20, textvariable=output_of_last_operation_variable)
output_of_last_operation_label.grid(column=0, row=0, columnspan=4, sticky=E) # STICKY????

# Creating label with result of calculating
result_of_operation = StringVar()
result_of_operation_entry = Label(mainframe, width=20, textvariable=result_of_operation)
result_of_operation_entry.grid(column=0, row=1, columnspan=4, sticky=E) # STICKY????

# Creating buttons
# + - * % backpase clear =
buttons_dict = {
    'button_plus' : {'text' : '+', 'command': lambda: operation_to_add(), 'column': 0, 'row':2},
    'button_minus': {'text' : '-', 'command': lambda: operation_to_minus(), 'column': 1, 'row':2},
    'button_divide': {'text' : '/', 'command': lambda: operation_to_divide(), 'column': 2, 'row':2},
    'button_multiply': {'text' : '*', 'command': lambda: operation_to_multiply(), 'column': 3, 'row':2},
    'button_number_0': {'text' : '0', 'command': lambda: insert_number(0), 'column': 1, 'row':6},
    'button_number_1': {'text' : '1', 'command': lambda: insert_number(1), 'column': 0, 'row':5},
    'button_number_2': {'text' : '2', 'command': lambda: insert_number(2), 'column': 1, 'row':5},
    'button_number_3': {'text' : '3', 'command': lambda: insert_number(3), 'column': 2, 'row':5},
    'button_number_4': {'text' : '4', 'command': lambda: insert_number(4), 'column': 0, 'row':4},
    'button_number_5': {'text' : '5', 'command': lambda: insert_number(5), 'column': 1, 'row':4},
    'button_number_6': {'text' : '6', 'command': lambda: insert_number(6), 'column': 2, 'row':4},
    'button_number_7': {'text' : '7', 'command': lambda: insert_number(7), 'column': 0, 'row':3},
    'button_number_8': {'text' : '8', 'command': lambda: insert_number(8), 'column': 1, 'row':3},
    'button_number_9': {'text' : '9', 'command': lambda: insert_number(9), 'column': 2, 'row':3},
    'button_comma': {'text' : ',', 'command': lambda: insert_number(','), 'column': 2, 'row':6},
    'button_plus_or_minus': {'text' : '+/-', 'command': lambda: change_sign(), 'column': 0, 'row':6},
    'button_x_squared': {'text' : 'x^2', 'command': lambda: operation_to_square(), 'column': 3, 'row':3},
    'button_square_root_of_x': {'text' : 'sqrt(x)', 'command': lambda: operation_to_square_root(), 'column': 3, 'row':4},
    'button_clear': {'text' : 'Clear', 'command': lambda: operation_to_clear(), 'column': 3, 'row':5},
    'button_equal': {'text' : '=', 'command': lambda: operation_to_equal(), 'column': 3, 'row':6},
}

for button in buttons_dict:
    Button(mainframe, text = buttons_dict[button]['text'],
    command = buttons_dict[button]['command']).grid(
        column = buttons_dict[button]['column'],
        row = buttons_dict[button]['row'],
        padx = 15,
        pady = 15
    )

root.mainloop()