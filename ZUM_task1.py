
# Projekt kalkulatora prostego sterowanego głosem przygotowany przez:
#  - Macieja Ostrowskiego
#  - Joannę Zalewską
 

from transformers import pipeline
import whisper
import speech_recognition as sr
import operator
import re
import requests

#audio1 = 'Downloads/recordings_divide.wav'

#function to test the model by user
def user_input_test():
    path = 'https://github.com/aexye/zum-pjatk/raw/main/recordings/'
    user_input_calc = input("Choose one from the list: add, substract, multiply, divide, squared: ")
    if user_input_calc in ('add', 'substract', 'multiply', 'divide', 'squared'):
        if user_input_calc == 'squared':
            calc = 'squared.wav'
            audio_url = path + calc
        elif user_input_calc == 'add':
            calc = 'plus.wav'
            audio_url = path + calc
        elif user_input_calc == 'substract':
            calc = 'minus.wav'
            audio_url = path + calc
        elif user_input_calc == 'multiply':
            calc = 'multiply.wav'
            audio_url = path + calc
        elif user_input_calc == 'divide':
            calc = 'divide.wav'
            audio_url = path + calc
        else:
            print("Wrong input, try again")

        print("You chose {}".format(user_input_calc))

        r = requests.get(audio_url, allow_redirects=True)
        open(calc, 'wb').write(r.content)

    return calc

# Record audio

def record_audio():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.record(source, duration=5)
    # write audio to a WAV file
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())
    audio = 'microphone-results.wav'
    print('Processing...')
    return audio





operators_list = ['add', 'sum', 'plus', '+', 'substract', 'difference', 'minus', '-', 'multiply','product', 'times', 'x', '*', '/', 'divide', 'divided', 'division', 'squared']

def get_info_from_input(voice_input_string):

    # operation_name = {
    #     '+': ['add', 'plus'],
    #     '-': ['substract', 'minus'],
    #     '*': ['times', 'multiply', 'product'],
    #     '/': ['divide']
    # } 

    voice_input_string = voice_input_string.lower()
    voice_input_string = re.sub(r'[^\w\s]', '', voice_input_string)

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

    if oper == 'squared':
        numbers.append(2)
    return oper, numbers



numbers_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20
    }

def operation_switch(operator_string):
    return  {
                # Addition
                'add': operator.add,
                'sum': operator.add,
                'plus': operator.add,
                '+': operator.add,
                # Subtraction
                'substract': operator.sub,
                'difference': operator.sub,
                'minus': operator.sub,
                '-': operator.sub,
                # Mnożenie
                'multiply': operator.mul,
                'product': operator.mul,
                'times': operator.mul,
                'x': operator.mul,
                '*': operator.mul, 
                # Dzielenie
                'divided': operator.truediv,
                'divide': operator.floordiv,
                'division': operator.floordiv,
                '/': operator.floordiv,
                #Kwadrat
                'squared': operator.pow
            }[operator_string]

def calculate(values):
    try:
        num1, num2 = get_info_from_input(values)[1]
        result = int(operation_switch(get_info_from_input(values)[0])(num1, num2))
        print("The result of your calculation is {}".format(result))
    except: 
        print("I don't know what the answer is, please use any of these words {} and numbers to operate.".format(operators_list))


if __name__ == "__main__":
    #Let user decide if he wants to use the model or record his own voice
    input_continue = True
    while input_continue == True:
        try:
            user_input = input("You want to say your calculation or just test an example? (calc/test) ")
            if user_input == 'test':
                audio = user_input_test()
            elif user_input == 'calc':
                audio = record_audio()
            user_input_model = input("Do you want to use the facebook model or the whisper? (fb/wh) ")
            if user_input_model == 'fb':
                pipe = pipeline(model="facebook/wav2vec2-large-960h-lv60-self", task='automatic-speech-recognition')
                result = pipe(audio)
            elif user_input_model == 'wh':
                model = whisper.load_model("base")
                result = model.transcribe(
                    audio, fp16=False, language="en")
                
            text = result['text'].lower()
            print(text)
            calculate(text)
            input_continue = input("Do you want to continue? (y/n) ")
            if input_continue == 'y':
                input_continue = True
        except:
            print("Something went wrong, try again")
            input_continue = input("Do you want to continue? (y/n) ")
            if input_continue == 'y':
                input_continue = True
