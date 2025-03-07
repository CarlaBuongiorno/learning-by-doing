from bitbucket import (get_author, get_commits_per_author,
                       get_customers, get_customer_path,
                       page_check)
from typing import Any

def test_get_author() -> None:
    obj = {'values': [{'author': {'name': 'iwan.intgroen', 'id': 133}, 'displayId': '87e9bd0bb60'},
                      {'author': {'name': 'pavlos.platanias', 'type': 'NORMAL'}, 'authorTimestamp': 1685616855000}]}
    expected_list = ['iwan.intgroen', 'pavlos.platanias']
    authors = get_author(obj)
    assert authors == expected_list

def test_get_author_dict() -> None:
    authors = ['iwan.intgroen', 'pavlos.platanias', 'pavlos.platanias']
    expected_dict = {'iwan.intgroen': 1, 'pavlos.platanias': 2}
    name_commits = get_commits_per_author(authors)
    assert name_commits == expected_dict

def test_get_customers() -> None:
    obj = {'values': [{'forkable': True, 'slug': 'blue'},
                    {'id': 29, 'slug': 'denim'}]}
    customers = get_customers(obj)
    assert customers == ['blue', 'denim']

def test_get_customer_path() -> None:
    customers = ['blue', 'denim']
    customer_paths = get_customer_path(customers)
    assert customer_paths == {'blue': '/blue/commits', 'denim': '/denim/commits'}

# def test_get_obj_list() -> None:
#     customer_paths = ['/blue/commits']
#     url = 'http://bitbucket/api'
#     path = '/CUSTOMER/repos'
#     args = {'start': 0}
#     headers = {'Auth': 'myToken'}

#     def fake_get_obj(u: str, a: dict[str, int], h: dict[str, str]) -> dict[str, str]:
#         assert a == args
#         assert h == headers
#         assert u == url+path+customer_paths[0]
#         return {'name': 'blue'}
    
#     obj_list = get_obj_list(customer_paths, url, path, args, headers, fake_get_obj)
#     assert obj_list == [{'name': 'blue'}]

def test_page_check() -> None:
    args = {'start': 0}
    obj_1 = {'isLastPage': False, 'start': 0, 'nextPageStart': 1}
    obj_2 = {'isLastPage': True, 'start': 1, 'nextPageStart': 2}
    is_last_page = False
    assert page_check(obj_1, args, is_last_page) == False
    assert page_check(obj_2, args, is_last_page) == True
