import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    #тест: первый символ - прописная буква
    ("skypro", "Skypro"),
    #тест: проверка не изменяется буква на заглавную после пробела
    ("hello world", "Hello world"),
    #тест: первый символ - пробел
    (" python", " python"),
        ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # первый символ не буква
    ("123abc", "123abc"),
    # пустая строка
    ("", ""),
    # строка из пробелов
    ("   ", "   "),
    #негативный тест: первая буква уже заглавная
    ("Python", "Python")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected



@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    #  один пробел в начале
     (" skypro", "skypro"),
    # несколько пробелов в начале
     ("    hello", "hello"),
     # пробелы в середине строки
     ("hello world", "hello world"),
    # пробелы в конце
     ("python    ", "python    "),
 ])
def test_trim_positive(input_str, expected):
     assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # нет пробелов в начале
     ("skypro", "skypro"),
    # пустая строка
     ("", ""),
    # точки в начале
     (".....python", ".....python"),
 ])
def test_trim_negative(input_str, expected):
     assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    # в строке содержится искомый символ
     ("skypro", "y"),
    # в строке содержится несколько искомых символов
     ("hello", "l"),
     # в строке содержится искомый символ, не являющийся буквой
     ("1234", "4"),
     ])
def test_contains_positive(input_str, symbol):
     assert string_utils.contains(input_str, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    # в строке не содержится искомый символ
     ("skypro", "n"),
    # в строке содержится искомый символ в другом регистре
     ("skypro", "Y"),
     ("Skypro", "s"),
    ])
def test_contains_negative(input_str, symbol):
     assert string_utils.contains(input_str, symbol) is False


@pytest.mark.positive
def test_delete_symbol_positive():
     # все подстроки удаляются из строки
     assert string_utils.delete_symbol("hello", "l") == "heo"
     # в строке удается подстрока, не являющаяся буквой
     assert string_utils.delete_symbol("1234", "4") == "123"
     # удаляются пробелы в начале, середине, конце
     assert string_utils.delete_symbol(" hello world ", " ") == "helloworld"

@pytest.mark.negative
def test_delete_symbol_negative():
     # удаление символа, которого нет в строке
    assert string_utils.delete_symbol("1234", "5") == "1234"
     # удаление символа из пустой строки
    assert string_utils.delete_symbol("", "!") == ""
       # удаление пустой подстроки
    assert string_utils.delete_symbol("hello world", "") == "hello world"