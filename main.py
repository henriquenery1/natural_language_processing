import requests
from deep_translator import GoogleTranslator

def get_data():
    url = 'https://api.chucknorris.io/jokes/random'
    r = requests.get(url)
    data = r.json()
    print(data['value'])
    return data['value']

def translate_text():
    translated = GoogleTranslator(source="en", target="pt").translate
    text = get_data()
    translated_text = translated(text)
    print(translated_text)

def main():
    translate_text()


if __name__ == '__main__':
    main()