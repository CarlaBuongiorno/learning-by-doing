import requests
from typing import Any


def main(token: str) -> None:
    url = 'https://bitbucket.detact.fox.local/rest'
    get_repos_path = '/api/latest/projects/CUSTOMER/repos'
    headers = {'Authorization': f'Bearer {token}'}
    args = {'start': 0, 'limit': 100}
    is_last_page = False
    customers = get_all_customers(url, get_repos_path, args, headers, is_last_page)
    customer_paths = get_customer_path(customers)
    for customer, customer_path in customer_paths.items():
        is_last_page = False
        commits_per_author = get_commits(is_last_page, url, get_repos_path, customer_path, args, headers)
        print(f'\nFor {customer}:')
        for author, commits in commits_per_author.items():
            print(f'{author} has made {commits} commits.')


def get_all_customers(url: str,
                      get_repos_path: str, 
                      args: dict[str, int], 
                      headers: dict[str, str], 
                      is_last_page: bool) -> list[str]:
    
    customers = []
    while not is_last_page:
        obj = get_obj(url+get_repos_path, args, headers=headers)
        customers.extend(get_customers(obj))
        is_last_page = page_check(obj, args, is_last_page)
    return customers


def get_obj(url: str, args: dict[str, int], headers: dict[str, str]) -> Any:
    return requests.get(url, params=args, headers=headers).json()


def get_customers(obj: Any) -> list[str]:
    return [customer['slug'] for customer in obj['values']]


def page_check(obj: Any, args: dict[str, int], is_last_page: bool) -> Any:
    if not obj['isLastPage']:
        args['start'] = obj['nextPageStart']
    else:
        args['start'] = 0
        is_last_page = True
    return is_last_page


def get_customer_path(customers: list[Any]) -> dict[str, str]:
    customer_paths = {}
    for customer in customers:
        customer_paths[customer] = f'/{customer}/commits'
    return customer_paths


def get_commits(is_last_page: bool,
                url: str,
                get_repos_path: str,
                customer_path: str,
                args: dict[str, int], 
                headers: dict[str, str]) -> dict[str, int]:
    
    authors_per_customer = []
    while not is_last_page:
        obj = get_obj(url+get_repos_path+customer_path, args, headers=headers)
        authors = get_author(obj)
        authors_per_customer.extend(authors)
        is_last_page = page_check(obj, args, is_last_page)
        commits_per_author = get_commits_per_author(authors_per_customer)
    return commits_per_author


def get_author(obj: dict[str, Any]) -> list[str]:
    return [author['author']['name'] for author in obj['values']]


def get_commits_per_author(authors: list[str]) -> dict[str, int]:
    name_commits = {}
    for name in authors:
        name_commits[name] = authors.count(name)
    return name_commits


if __name__ == '__main__':
    import os
    token = os.environ['SECRET_TOKEN']
    main(token)
