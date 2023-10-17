import requests
from typing import Any


def main() -> None:
    url = 'https://bitbucket.detact.fox.local/rest'
    path = '/api/latest/projects/CUSTOMER/repos'
    headers = {'Authorization': 'Bearer ThisIsNotMyRealBearerToken'}
    args = {'start': 0, 'limit': 50}
    r = requests.get(url+path, headers=headers)
    customers = get_customer(r.json())
    customer_paths = get_customer_path(customers)
    obj_list = get_obj(customer_paths, url, path, args, headers)
    authors = get_author(obj_list)
    name_commits = get_author_dict(authors)
    # while not obj_list['isLastPage']:
    #     args['start'] = obj_list['nextPageStart']
    for name in name_commits:
        print(f'{name} made {name_commits[name]} commits')


def get_customer_path(customers: list[Any]) -> list[str]:
    customer_paths = [f'/{customer}/commits' for customer in customers]
    return customer_paths


def get_customer(obj: Any) -> list[str]:
    customers = [customer['slug'] for customer in obj['values']]
    return customers


def get_obj(customer_paths: list[str], url: str, path: str, args: dict[str, int], headers: dict[str, str]) -> list[Any]:
    obj_list = [requests.get(url+path+customer_path, params=args, headers=headers).json() for customer_path in customer_paths]
    obj = [obj for obj in obj_list]
    return obj


def get_author(obj_list: list[dict[str, list[Any]]]) -> list[str]:
    authors = [author['author']['name'] for obj in obj_list for author in obj['values']]
    return authors


def get_author_dict(authors: list[str]) -> dict[str, int]:
    name_commits = {}
    for name in authors:
        name_commits[name] = authors.count(name)
    return name_commits


if __name__ == '__main__':
    main()
