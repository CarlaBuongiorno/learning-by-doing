from pure_rummy import rummy


INVALID = 'Sorry, that is invalid'

def test_input_invalid_none():
    compare_input_with_expected_output(None)

def test_input_invalid_empty_string():
    compare_input_with_expected_output('')

def test_input_invalid_integer():
    compare_input_with_expected_output(5)

def test_input_invalid_list():
    compare_input_with_expected_output([])

def test_input_invalid_not_seven_cards():
    compare_input_with_expected_output('2H 3D 4S 5H 4H JC')

def test_input_invalid_potato():
    compare_input_with_expected_output('potatopotato')

def test_input_invalid_seven_cards():
    compare_input_with_expected_output('AH 2H 3H 4B 5H 6H 7H')

def test_input_valid_cards_lose():
    compare_input_with_expected_output('3C 3D 3H 3S 4S 5C 6S', 'LOSE')

def test_input_valid_cards_lose_v2():
    compare_input_with_expected_output('QC KC AC AS 2S 3S 4S', 'LOSE')

def compare_input_with_expected_output(user_input, output=INVALID):
    result = rummy(user_input)
    assert result == output