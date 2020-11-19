import sys
from translate import Translator

lang =  sys.argv[1]

try:
    with open('text.txt', mode='r') as my_file:
        text = my_file.read()
        translator = Translator(to_lang=lang)
        translation = translator.translate(text)
        with open(f'text-{lang}.txt', mode='w') as trans_file:
            trans_file.write(translation)
except FileNotFoundError as err:
    print('File not found')
