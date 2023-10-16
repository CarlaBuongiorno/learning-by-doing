from bitbucket import get_author, get_author_dict

def test_get_author():
    obj = {'values': [
        {'author': {'name': 'iwan.intgroen'}},
        {'author': {'name': 'pavlos.platanias'}}
        ]}
    expected_list = ['iwan.intgroen', 'pavlos.platanias']
    authors = get_author(obj)
    assert authors == expected_list

def test_get_author_dict():
    authors = ['iwan.intgroen', 'pavlos.platanias', 'pavlos.platanias']
    expected_dict = {'iwan.intgroen': 1, 'pavlos.platanias': 2}
    name_commits = get_author_dict(authors)
    assert name_commits == expected_dict