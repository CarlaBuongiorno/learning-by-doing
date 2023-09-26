from advice_api import get_random_advice, get_advice_by_id

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
