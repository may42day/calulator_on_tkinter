from tkinter import *

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

def do_previous_opperation(sign):
    global last_operation

    if len(result_of_operation.get()) == 0:
        pass
    else:
        current_number = correct_number_value(result_of_operation.get())
        if sign == '+':
            result = saved_number + current_number
        elif sign == '-':
            result = saved_number - current_number
        elif sign == '/':
            try :
                result = saved_number / current_number
            except ZeroDivisionError:
                operation_to_clear()
                global saved_second_number
                return None  
        elif sign == '*':
            result = saved_number * current_number
        elif sign == '=':
            pass
        if sign != 'sqr' and sign != 'sqrt':
            result_of_operation.set(str(result).replace('.', ','))

def operation_with_sign(sign):
    global last_operation
    global saved_number
    
    if len(result_of_operation.get()) == 0 and len(last_operation) == 0:
        pass  
    elif len(last_operation) == 0:
        last_operation = sign
        saved_number = correct_number_value(result_of_operation.get())
        output_of_last_operation_variable.set(f'{saved_number} {sign} ')
        result_of_operation.set('')
    elif len(result_of_operation.get()) == 0:
        last_operation = sign
        new_output = f'{saved_number} {sign} '
        output_of_last_operation_variable.set(new_output)
    elif sign == '=':
        saved_second_number = correct_number_value(result_of_operation.get())
        if last_operation != 'sqrt' and last_operation != 'sqr':
            do_previous_opperation(last_operation)
            output_of_last_operation_variable.set(f'{saved_number} {last_operation} {saved_second_number} = ')
        else:
            output_of_last_operation_variable.set(f'{last_operation} of {saved_number} = ')
        last_operation = ""
        saved_number = correct_number_value(result_of_operation.get())
    else:
        do_previous_opperation(last_operation)
        last_operation = sign
        output_of_last_operation_variable.set(f'{result_of_operation.get()} {sign} ')
        saved_number = correct_number_value(result_of_operation.get())
        result_of_operation.set('')

def operation_to_square():
    global last_operation
    global saved_number

    if len(last_operation) != 0:
        do_previous_opperation(last_operation)
    elif len(result_of_operation.get()) == 0:
        pass
    else:
        saved_number = correct_number_value(result_of_operation.get())
        output_of_last_operation_variable.set(f'{saved_number}²')
        result = str(saved_number ** 2).replace('.', ',')
        result_of_operation.set(result)
        last_operation = 'sqr'

def operation_to_square_root():
    global last_operation
    global saved_number

    if len(last_operation) != 0:
        do_previous_opperation(last_operation)
    elif len(result_of_operation.get()) == 0:
        pass
    else:
        saved_number = correct_number_value(result_of_operation.get())
        output_of_last_operation_variable.set(f'√{saved_number} =')
        result = str(saved_number ** 0.5).replace('.', ',')
        last_operation = 'sqrt'
        if result[-1] == '0':
            result_of_operation.set(result[:-2])
        else:
            result_of_operation.set(result)

def operation_to_clear():
    global saved_number
    global last_operation
    
    result_of_operation.set('')
    output_of_last_operation_variable.set('')
    saved_number = 0    
    last_operation = ''

# Colors for elements
color_main_background = '#9da0a6'
color_output_of_last_operation = '#9da0a6'
color_result_of_operation = '#727987'
color_background_of_button_number = 'white'
color_activebackground_of_button_number = '#c2c5cb'
color_background_of_button_sign = '#958ad7'
color_activebackground_of_button_sign = '#b3aed1'


root = Tk()
root.title("Calculator")
root.geometry('290x345+100+100')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variables
saved_number = 0    
last_operation = '' 
output_of_last_operation_variable = StringVar()
result_of_operation = StringVar()

mainframe = Frame(root, background=color_main_background)
mainframe.grid(column=0, row=0,sticky=(N, W, E, S))

for column in range(4):
    mainframe.columnconfigure(column, weight = 1)

for row in range(7):
    mainframe.rowconfigure(row, weight=1)


output_of_last_operation_label = Label(mainframe,background=color_output_of_last_operation, textvariable=output_of_last_operation_variable, width=22, height=1, font = 'Arial 10', anchor= E)
output_of_last_operation_label.grid(column=0, row=0, columnspan=4, padx=10, pady=5, sticky=(N, W, E, S))


result_of_operation_label = Label(mainframe, background=color_result_of_operation, textvariable=result_of_operation, width=19, height=1, font = 'Arial 18', anchor= E)
result_of_operation_label.grid(column=0, row=1, columnspan=4, padx=10, pady=5, sticky=(N, W, E, S))

buttons_dict = {
    'button_plus' : {'text' : '+', 'command': lambda: operation_with_sign('+'), 'column': 0, 'row':2, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_minus': {'text' : '-', 'command': lambda: operation_with_sign('-'), 'column': 1, 'row':2, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_divide': {'text' : '/', 'command': lambda: operation_with_sign('/'), 'column': 2, 'row':2, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_multiply': {'text' : '*', 'command': lambda: operation_with_sign('*'), 'column': 3, 'row':2, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_number_0': {'text' : '0', 'command': lambda: insert_number(0), 'column': 1, 'row':6, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_1': {'text' : '1', 'command': lambda: insert_number(1), 'column': 0, 'row':5, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_2': {'text' : '2', 'command': lambda: insert_number(2), 'column': 1, 'row':5, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_3': {'text' : '3', 'command': lambda: insert_number(3), 'column': 2, 'row':5, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_4': {'text' : '4', 'command': lambda: insert_number(4), 'column': 0, 'row':4, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_5': {'text' : '5', 'command': lambda: insert_number(5), 'column': 1, 'row':4, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_6': {'text' : '6', 'command': lambda: insert_number(6), 'column': 2, 'row':4, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_7': {'text' : '7', 'command': lambda: insert_number(7), 'column': 0, 'row':3, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_8': {'text' : '8', 'command': lambda: insert_number(8), 'column': 1, 'row':3, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_number_9': {'text' : '9', 'command': lambda: insert_number(9), 'column': 2, 'row':3, 'background':color_background_of_button_number , 'activebackground': color_activebackground_of_button_number},
    'button_comma': {'text' : ',', 'command': lambda: insert_number(','), 'column': 2, 'row':6, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_plus_or_minus': {'text' : '+/-', 'command': lambda: change_sign(), 'column': 0, 'row':6, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_x_squared': {'text' : 'x²', 'command': lambda: operation_to_square(), 'column': 3, 'row':3, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_square_root_of_x': {'text' : '√x', 'command': lambda: operation_to_square_root(), 'column': 3, 'row':4, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_clear': {'text' : 'C', 'command': lambda: operation_to_clear(), 'column': 3, 'row':5, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
    'button_equal': {'text' : '=', 'command': lambda: operation_with_sign('='), 'column': 3, 'row':6, 'background':color_background_of_button_sign , 'activebackground': color_activebackground_of_button_sign},
}

# Draw all buttons
for button in buttons_dict:
    Button(mainframe, text = buttons_dict[button]['text'],
    command = buttons_dict[button]['command'],
    foreground="black", background=buttons_dict[button]['background'], 
    width = 6, height = 2,
    font = 'Arial 13 bold', relief = FLAT, bd = 0,
    activebackground = buttons_dict[button]['activebackground']
    ).grid(
        column = buttons_dict[button]['column'],
        row = buttons_dict[button]['row'],
        padx = 3, pady = 3,
        sticky=(N, W, E, S)
    )


root.mainloop()