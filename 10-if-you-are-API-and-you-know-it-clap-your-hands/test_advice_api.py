from advice_api import (get_random_advice, get_advice_by_id,
                        get_advice_by_keyword, OptionPicker)

def test_get_random_advice():
    url = 'http://great.advice.com'
    expected_advice = 'Treat your cats nicely, they hunt you in your sleep.'

    def fake_get_obj(u):
        assert u == url
        return {'slip': {'advice': expected_advice} }

    advice, continue_running = get_random_advice(url, fake_get_obj)
    assert advice == expected_advice
    assert continue_running


def test_get_advice_by_id():
    url = 'http://the.same.com'
    expected_advice = 'Never learn AngularJS.'
    advice_id = '72'

    def fake_input(prompt):
        assert prompt == 'Enter the ID number of the advice you wish to see: '
        return advice_id

    def fake_get_obj(u):
        assert u == f'{url}/{advice_id}'
        return {'slip': {'advice': expected_advice} }

    advice, continue_running = get_advice_by_id(url, fake_get_obj, fake_input)
    assert advice == expected_advice
    assert continue_running


def test_get_advice_by_keyword():
    url = 'http://my.version.com'
    expected_advice_1 = 'Make your bed.'
    expected_advice_2 = 'Tidy your bedroom.'
    expected_advice = f'{expected_advice_1}\n{expected_advice_2}'
    advice_keyword = 'bed'

    def fake_input(prompt):
        assert prompt == 'Enter your keyword: '
        return advice_keyword

    def fake_get_obj(u):
        assert u == url + '/search/' + advice_keyword
        return {'slips': [{'advice': expected_advice_1}, {'advice': expected_advice_2}] }
    
    advice, continue_running = get_advice_by_keyword(url, fake_get_obj, fake_input)
    assert advice == expected_advice
    assert continue_running


def test_get_advice_by_keyword_no_match():
    url = 'http://second.version.com'
    advice_keyword = 'bed'
    no_match = 'No advice slips found matching that search term.'

    def fake_input(prompt):
        assert prompt == 'Enter your keyword: '
        return advice_keyword

    def fake_get_obj(u):
        assert u == url + '/search/' + advice_keyword
        return {'message': {'text': no_match} }
    
    advice, continue_running = get_advice_by_keyword(url, fake_get_obj, fake_input)
    assert advice == no_match
    assert continue_running

def test_advice_option():
    url = 'http://my.version.com'
    expected_advice = 'Make your bed.'

    def bad_function(url):
        assert False

    def good_function(url):
        return expected_advice

    test_functions = [bad_function, bad_function, good_function]
    picker = OptionPicker(test_functions)
    assert expected_advice == picker.get_advice_by_id(3, url)