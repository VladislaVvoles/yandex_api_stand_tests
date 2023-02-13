import sender_stand_request
import data

#Допустимое количество символов (2)
def get_user_body(first_name):

    current_body = data.user_body.copy()

    current_body["firstName"] = first_name

    return current_body

def test_create_user_1_letter_in_first_name_get_error_response():

    user_body = get_user_body("А")

    user_response = sender_stand_request.post_new_user(user_body)


    assert user_response.status_code == 400

    assert user_response.json()["code"] == 400


    assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                             "Имя может содержать только русские или латинские буквы, " \
                                             "длина должна быть не менее 2 и не более 15 символов"

    print(user_response.headers)
    print(user_response.text)

def test_create_user_16_letter_in_first_name_get_error_response():

    user_body = get_user_body("Аaaaaaaaaaaaaaaa")

    user_response = sender_stand_request.post_new_user(user_body)


    assert user_response.status_code == 400

    assert user_response.json()["code"] == 400


    assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                             "Имя может содержать только русские или латинские буквы, " \
                                             "длина должна быть не менее 2 и не более 15 символов"

    print(user_response.headers)
    print(user_response.text)

def test_create_user_has_space_in_first_name_get_error_response():

    user_body = get_user_body("Человек и Ко")

    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400

    assert user_response.json()["code"] == 400

    assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                              "Имя может содержать только русские или латинские буквы, " \
                                              "длина должна быть не менее 2 и не более 15 символов"

    print(user_response.headers)
    print(user_response.text)

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    user_body = get_user_body("№%@")

    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400

    assert user_response.json()["code"] == 400

    assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                              "Имя может содержать только русские или латинские буквы, " \
                                              "длина должна быть не менее 2 и не более 15 символов"

    print(user_response.headers)
    print(user_response.text)

def test_create_user_has_number_in_first_name_get_error_response():
    user_body = get_user_body("123")

    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400

    assert user_response.json()["code"] == 400

    assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                              "Имя может содержать только русские или латинские буквы, " \
                                              "длина должна быть не менее 2 и не более 15 символов"

    print(user_response.headers)
    print(user_response.text)


def test_create_user_no_first_name_get_error_response():

    user_body = data.user_body.copy()
    user_body.pop("firstName")

    negative_assert_no_firstname(user_body)

def negative_assert_no_firstname(user_body):

    response = sender_stand_request.post_new_user(user_body)

    assert response.json()["code"] == 400

    assert response.json()["message"] == "Не все необходимые параметры были переданы"

    print(response.headers)
    print(response.text)

def test_create_user_has_0_symbols_in_first_name_get_error_response():
    user_body = get_user_body("")

    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400

    assert user_response.json()["code"] == 400

    assert user_response.json()["message"] == "Не все необходимые параметры были переданы"

    print(user_response.headers)
    print(user_response.text)

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)

    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400

    print(user_response.headers)
    print(user_response.text)