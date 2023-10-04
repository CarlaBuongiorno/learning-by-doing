import requests
import subprocess


def get_obj(url):
    r = requests.get(url)
    obj = r.json()
    return obj


def main(data_retriever=get_obj, outputter=subprocess.run):
    url = 'https://coffee.alexflipnote.dev/random.json'
    r = data_retriever(url)
    image = get_image(r)
    outputter(['firefox', image])


def get_image(obj):
    return obj['file']


if __name__ == '__main__':
    main()