import requests


def main():
    url = 'https://evilinsult.com/generate_insult.php'
    arguments = {'lang': 'en', 'type': 'json'}
    for i in range(1, 6):
        r = requests.get(url, params=arguments)
        obj = r.json()
        print(f'{i}. {obj["insult"]}')


if __name__ == '__main__':
    main()
