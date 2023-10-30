import requests
from typing import Any


def main(token) -> None:
    url = 'https://bitbucket.detact.fox.local/rest'
    get_repos_path = '/api/latest/projects/CUSTOMER/repos'
    headers = {'Authorization': f'Bearer {token}'}
    args = {'start': 0, 'limit': 100}
    is_last_page = False
    customers = []
    while not is_last_page:
        obj = get_obj(url+get_repos_path, args, headers=headers)
        customers.extend(get_customers(obj))
        is_last_page = get_all_pages(obj, args, is_last_page)
        
    customer_paths = get_customer_path(customers) # {'blue': '/blue/commits', 'denim': '/denim/commits', 'emerald': '/emerald/commits', 'emeraldmoss': '/emeraldmoss/commits', 'lilac': '/lilac/commits', 'neon': '/neon/commits', 'robijn': '/robijn/commits', 'sapphire': '/sapphire/commits', 'scarlet': '/scarlet/commits', 'silver': '/silver/commits'}

    for customer in customer_paths.keys():
        is_last_page = False
        author_list = []
        while not is_last_page:
            obj = get_obj(url+get_repos_path+customer_paths[customer], args, headers=headers) # {'values': [{'id': 'd3f606feb439', 'author': {'name': 'Berend Botje'}, 'authorTimestamp': 169814032, 'committer': {'name': 'Berend Botje'}, 'committerTimestamp': 169811000, 'message': 'Bump version to 15.55}], 'size': 1, 'isLastPage': False, 'start': 0, 'limit': 1, 'nextPageStart': 1}
            authors = get_author(obj)
            author_list.extend(authors)
            is_last_page = get_all_pages(obj, args, is_last_page)
            author_dict = get_author_dict(author_list)

        print(f'\nFor {customer}:')
        for author, commits in author_dict.items():
            print(f'{author} has made {commits} commits.')


def get_obj(url: str, args: dict[str, int], headers: dict[str, str]) -> dict[str, Any]:
    return requests.get(url, params=args, headers=headers).json()


def get_customers(obj: Any) -> list[str]:
    return [customer['slug'] for customer in obj['values']]


def get_customer_path(customers: list[Any]) -> dict[str, str]:
    customer_paths = {}
    for customer in customers:
        customer_paths[customer] = f'/{customer}/commits'
    return customer_paths


def get_obj_list(customer_paths: list[str], url: str, path: str, args: dict[str, int], headers: dict[str, str], data_retriever=get_obj) -> list[Any]:
    return [data_retriever(url+path+customer_path, args, headers) for customer_path in customer_paths]


def get_author(obj: list[dict[str, list[Any]]]) -> list[str]:
    return [author['author']['name'] for author in obj['values']]


def get_author_dict(authors: list[str]) -> dict[str, int]:
    name_commits = {}
    for name in authors:
        name_commits[name] = authors.count(name)
    return name_commits


def get_all_pages(obj, args, is_last_page):
    if not obj['isLastPage']:
        args['start'] = obj['nextPageStart']
    else:
        args['start'] = 0
        is_last_page = True
    return is_last_page


if __name__ == '__main__':
    import os
    token = os.environ['SECRET_TOKEN']
    main(token)
