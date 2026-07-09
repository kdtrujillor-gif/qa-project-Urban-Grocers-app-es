import data
import sender_stand_request

def get_kit_body(kit_name):
    current_body = data.Kit_body.copy()
    current_body['name'] = kit_name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()['authToken']

def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201

def negative_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


def test_1_kit_name_with_1_letter():
    positive_assert('a')

def test_2_kit_name_with_511_letter():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_3_kit_name_with_0_letter():
    negative_assert("")

def test_4_kit_name_with_512_letter():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_5_kit_name_with_special_characters_letter():
    positive_assert("№%@,")

def test_6_kit_name_with_spaces_are_allowed_letter():
    positive_assert("A Aaa")

def test_7_kit_name_with_number_letter():
    positive_assert("123")

def test_8_kit_name_param_is_not_passed_in_the_request():
    negative_assert({})

def test_9_kit_name_different_param_type_has_been_passed():
    negative_assert(123)
