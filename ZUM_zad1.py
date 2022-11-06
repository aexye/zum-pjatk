# %%
#Importing all needed packages
import re
import operator

def get_info_from_input(voice_input_string):

    # operation_name = {
    #     '+': ['dodać', 'plus'],
    #     '-': ['odjąć', 'minus'],
    #     '*': ['razy', 'pomnożyć', 'przemnożyć'],
    #     '/': ['podzielić']
    # }  
    oper = ''
    numbers = [] 

    for word in voice_input_string.split():
        if word in operators_list:
            oper = word
        elif word.isdigit():
            word = int(word)
            numbers.append(word)
        elif word in list(numbers_dict.keys()):
            numbers.append(int(numbers_dict[word]))

    if oper == 'kwadratu':
        numbers.append(2)
    return oper, numbers

operators_list = ['dodać', 'dodaj', 'plus', '+', 'odjąć', 'odejmij', 'minus', '-', 'pomnożyć','przemnożyć', 'pomnóż', 'razy', 'x', '*', '/', 'podzielić', 'podziel', 'podzielone', 'kwadratu']

numbers_dict = {
    'jeden': 1,
    'dwa': 2,
    'trzy': 3,
    'cztery': 4,
    'pięć': 5,
    'sześć': 6,
    'siedem': 7,
    'osiem': 8,
    'dziewięć': 9,
    'dziesięć': 10,
    'jedynaście': 11,
    'dwanaście': 12,
    'trzynaście': 13,
    'czternaście': 14,
    'pietnaście': 15,
    'szesnaście': 16,
    'siedemnaście': 17,
    'osiemnaście': 18,
    'dziewiętnaście': 19,
    'dwadzieścia': 20
    }

def operation_switch(operator_string):
    return  {
                # Addition
                'dodać': operator.add,
                'dodaj': operator.add,
                'plus': operator.add,
                '+': operator.add,
                # Subtraction
                'odjąć': operator.sub,
                'odejmij': operator.sub,
                'minus': operator.sub,
                '-': operator.sub,
                # Mnożenie
                'pomnożyć': operator.mul,
                'pomnóż': operator.mul,
                'przemnożyć': operator.mul,
                'pomnożone': operator.mul,
                'razy': operator.mul,
                'x': operator.mul,
                '*': operator.mul, 
                # Dzielenie
                'podzielić': operator.floordiv,
                'podziel': operator.floordiv,
                'podzielone': operator.floordiv,
                '/': operator.floordiv,
                #Kwadrat
                'kwadratu': operator.pow
            }[operator_string]

def calculate(values):
    try:
        num1, num2 = get_info_from_input(values)[1]
        result = operation_switch(get_info_from_input(values)[0])(num1, num2)
        return result
    except: 
        print("I don't know what's the answer is, please use any of these words {} and numbers to operate.".format(operators_list))
    
    

calculate('10 podzielone przez dwa')
calculate('2 do kwadratu')



