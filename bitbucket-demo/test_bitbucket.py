from bitbucket import (get_author, get_author_dict,
                       get_customer, get_customer_path)
from typing import Any

def test_get_author() -> None:
    obj_list = [{'values': [{'author': {'name': 'iwan.intgroen', 'id': 133}, 'displayId': '87e9bd0bb60'},
                            {'author': {'name': 'pavlos.platanias', 'type': 'NORMAL'}, 'authorTimestamp': 1685616855000}]},
                 {'values': [{'author': {'name': 'joris.vandenoever', 'id': 143}, 'displayId': '87e9bd0ba60'},
                            {'author': {'name': 'pavlos.platanias', 'type': 'NORMAL'},'authorTimestamp': 1685616855009}]}]
    expected_list = ['iwan.intgroen', 'pavlos.platanias', 'joris.vandenoever', 'pavlos.platanias']
    authors = get_author(obj_list)
    assert authors == expected_list

def test_get_author_dict() -> None:
    authors = ['iwan.intgroen', 'pavlos.platanias', 'pavlos.platanias']
    expected_dict = {'iwan.intgroen': 1, 'pavlos.platanias': 2}
    name_commits = get_author_dict(authors)
    assert name_commits == expected_dict

def test_get_customer() -> None:
    obj = {'values': [ {'forkable': True, 'slug': 'blue'},
                             {'id': 29, 'slug': 'denim'}]}
    expected_customers = ['blue', 'denim']
    customers = get_customer(obj)
    assert customers == expected_customers

def test_get_customer_path() -> None:
    customers = ['blue', 'denim']
    customer_paths = get_customer_path(customers)
    assert customer_paths == ['/blue/commits', '/denim/commits']

# def test_get_obj():
#     expected_url = 'http://bitbucket.com'
#     path = '/api/CUSTOMER/repos'
#     args = {'start': 0, 'limit': 2}
#     headers = {'Authorization': 'Bearer MFqcuiLq5eiGYVwz77vzJj1J'}
#     customer_paths = ['/blue/commits', '/denim/commits']
#     obj = get_obj(customer_paths, expected_url, path, args, headers)

