import requests
from pprint import pprint

def main():
    url = 'https://bitbucket.detact.fox.local/rest'
    path = '/api/latest/projects/CUSTOMER/repos/sapphire/commits'

    args = {'start': 0, 'limit': 50}
    headers = {'Authorization': 'Bearer Mzg2NTMxNzI4NDEwOqfEtFqcuiLq5eiGYVwz77vzJj1J'}

    r = requests.get(url+path, params=args, headers=headers)

    authors = get_author(r.json())
    print(authors)
    name_commits = get_author_dict(authors)
    
    for name in name_commits:
        print(f'{name} made {name_commits[name]} commits')
    

def get_author(obj):
    authors = [author['author']['name'] for author in obj['values']]
    return authors

def get_author_dict(authors):
    name_commits = {}
    for name in authors:
        name_commits[name] = authors.count(name)
    return name_commits


if __name__ == '__main__':
    main()