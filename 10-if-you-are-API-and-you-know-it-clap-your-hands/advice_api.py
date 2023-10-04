import requests

# Honestly, I wouldn't test this either
def main():
    url = 'https://api.adviceslip.com/advice'
    options = OptionPicker([get_random_advice, get_advice_by_id, get_advice_by_keyword, quit])
    main_menu = True
    while main_menu:
        print('1. Random piece of advice\n2. Get advice by ID\n3. Search by keyword\n4. Quit\n')
        menu_number = int(input('Choose a menu option: '))
        advice, main_menu = options.get_advice_by_id(menu_number, url)
        print(advice, end='\n\n')

class OptionPicker:
    def __init__(self, advice_options) -> None:
        self.advice_options = advice_options

    def get_advice_by_id(self, option_input, url):
        return self.advice_options[option_input -1](url)
    
# Don't test this, it's not worth it
def get_obj(url):
    r = requests.get(url)
    obj = r.json()
    return obj

def get_random_advice(url, data_retriever=get_obj):
    obj = data_retriever(url)
    return obj['slip']['advice'], True

def get_advice_by_id(url, data_retriever=get_obj, prompter=input):
    id = prompter('Enter the ID number of the advice you wish to see: ')
    combined_url = f'{url}/{id}'
    obj = data_retriever(combined_url)
    return obj['slip']['advice'], True

def get_advice_by_keyword(url, data_retriever=get_obj, prompter=input):
    keyword = prompter('Enter your keyword: ')
    keyword_url = url + '/search/' + keyword
    obj = data_retriever(keyword_url)
    if 'message' in obj:
        return obj['message']['text'], True
    else:
        return '\n'.join([adv['advice'] for adv in obj['slips']]), True

def quit(url):
    return f'Quit Program', False

if __name__ == '__main__':
    main()
