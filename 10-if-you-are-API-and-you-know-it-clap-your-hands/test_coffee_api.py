from coffee_api import get_image, main

def test_get_image():
    obj = {'file': 'https://coffee.com/coffee.jpg'}
    image = get_image(obj)
    assert image == obj['file']

def test_main():
    expected_url = 'https://coffee.alexflipnote.dev/random.json'
    expected_parameters = ['firefox', 'https://coffee.com/coffee.jpg']

    def fake_get_obj(u):
        # u is the real data
        assert u == expected_url
        return {'file': 'https://coffee.com/coffee.jpg'}
    
    def fake_outputter(p):
        # p is the subprocess.run which is called as 'outputter()'
        assert p == expected_parameters

    # call main with 2 fake functions as parameters
    main(fake_get_obj, fake_outputter) 