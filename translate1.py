import gtts

def read_from_file():
    global words_bank

    f= open('C:/Users/Arman/OneDrive/Desktop/DL/Assignment-8/translate.txt', 'r')
    temp = f.read().split('/n')

    words_bank = []

    for i in range(0,len(temp) - 1,2):
        my_dict = {'en': temp[i], 'fa': temp[i+1]}
        words_bank.append(my_dict)
    f.close()
    
def show_menu():
    print('welcome to the Translator')
    print('1 - Translate English to Persian')
    print('2 - Translate Persian to English') 
    print('3 - Add new word to database')
    print('4 - Exit') 

    



def translate_en_to_fa():
    output = ''
    user_text = input('Enter your English text: ')
    user_words = user_text.split(' ')
    for user_word in user_words:
        for word in words_bank:
            if user_word == word['en']:
                output = output + word['fa'] + ' '
                break
        else:
            output = output + user_word + ' '
    vv = gtts.gTTS(output, lang = 'ar')
    vv.save('Farsi.mp3')
    print(output)


def translate_fa_to_en():
    output = ''
    user_text = input('Enter your Farsi text: ')
    if '.' in user_text:
        user_sen = user_text.split('.')
        user_words = user_sen.split(' ')
    else:
        user_words = user_text.split(' ')
    for user_word in user_words:
        for word in words_bank:
            if user_word == word['fa']:
                output = output + word['en'] + ' '
                break
        else:
            output = output + user_word + ' '
    vv = gtts.gTTS(output, lang = 'en')
    vv.save('English.mp3')    
    print(output)

def add_new_word():
    new_word = input('Enter the English word you want to add to the Dictionary: ')
    new_trans = input('Enter the Farsi Translation of the word in English type: ')
    new_dict = {'en': new_word, 'fa': new_trans}
    words_bank.append(new_dict)
    f = open('C:/Users/Arman/OneDrive/Desktop/DL/Assignment-8/translate.txt', 'a')
    f.write(new_word)
    f.write(new_trans)
    f.close()


read_from_file()

while True:
    show_menu()
    choice = int(input('Enter your Choice: '))

    if choice == 1:
        translate_en_to_fa()
    elif choice == 2:
        translate_fa_to_en()
    elif choice == 3:
        add_new_word()
    elif choice == 4:
        exit(0)
        break
        