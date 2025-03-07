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

def test_input_valid_LOSE():
    compare_input_with_expected_output('2H 7D 4S 5H 4H JC 9C', 'LOSE')

def test_input_valid_WIN_straight_4_and_3_of_a_kind():
    compare_input_with_expected_output('AC AS 5C 8C 6C 7C AH', 'WIN')

def test_input_valid_WIN_straight_4_and_3_of_a_kind_letter_ranks():
    compare_input_with_expected_output('AC AS 8C 9C JC 10C AH', 'WIN')

def test_input_valid_WIN_straight_4_and_3_of_a_kind_letter_ranks_no_numbers():
    compare_input_with_expected_output('AC AS AD QC KC JC 10C', 'WIN')

def test_input_valid_WIN_straight_4_and_3_of_a_kind_letter_ranks_numbers_for_same_kind():
    compare_input_with_expected_output('2C 2S 2D QC KC JC 10C', 'WIN')

def test_input_valid_WIN_straight_3_and_4_of_a_kind():
    compare_input_with_expected_output('AC AS AD 8C 6C 7C AH', 'WIN')

def test_input_valid_WIN_straight_3_and_4_of_a_kind_letter_ranks():
    compare_input_with_expected_output('AC AS AD 9C JC 10C AH', 'WIN')

def test_input_valid_WIN_straight_3_and_4_of_a_kind_letter_ranks_no_numbers():
    compare_input_with_expected_output('AC AS AD QC KC JC AH', 'WIN')

def test_input_valid_WIN_straight_3_and_4_of_a_kind_letter_ranks_numbers_for_same_kind():
    compare_input_with_expected_output('2C 2S 2D QC KC JC 2H', 'WIN')

def compare_input_with_expected_output(user_input, output=INVALID):
    result = rummy(user_input)
    assert result == output