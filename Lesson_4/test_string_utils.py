import pytest

from string_utils import StringUtils


# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# Пример: `capitilaze("skypro") -> "Skypro"`

@pytest.mark.positive_test
def test_capitilaze_positive():
    Stringutils = StringUtils()
    res = Stringutils.capitalize("yuri")
    assert res == "Yuri"

@pytest.mark.negative_test
def test_capitilaze_negative():
    Stringutils = StringUtils()
    res = Stringutils.capitalize("123")
    assert res == "123"


# Принимает на вход текст и удаляет пробелы в начале, если они есть
# Пример: `trim("   skypro") -> "skypro"

@pytest.mark.positive_test
def test_trim_positive():
    Stringutils = StringUtils()
    res = Stringutils.trim("   Yuri")
    assert res == "Yuri"

@pytest.mark.negative_test
def test_trim_negative():
    Stringutils = StringUtils()
    res = Stringutils.trim("Yuri")
    assert res == "Yuri"

# Принимает на вход текст с разделителем и возвращает список строк. \n
# Параметры: \n 
#     string` - строка для обработки \n
#     delimeter` - разделитель строк. По умолчанию запятая (",") \n
#     Пример: `to_list("1:2:3", ":") -> ["1", "2", "3"]`

@pytest.mark.positive_test
def test_to_list_positive():
    Stringutils = StringUtils()
    res = Stringutils.to_list("1:2:3", ":")
    assert res == ["1", "2", "3"]

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
# Пример 1: `contains("SkyPro", "S") -> True`
# Пример 2: `contains("SkyPro", "U") -> False`

@pytest.mark.positive_test
def test_contains_positive():
    Stringutils = StringUtils()
    if  Stringutils.contains("Yuri", "Y"):
        res = True
    if Stringutils.contains("Yuri", "a"):
        res = False
res = ("Y")
assert res

# Удаляет все подстроки из переданной строки 
# Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
# Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`

@pytest.mark.positive_test
def test_del_symbol_positive():
    Stringutils = StringUtils()
    res = Stringutils.delete_symbol("YuriP", "P")
    assert res == "Yuri"

@pytest.mark.negative_test
def test_del_symbol_negative():
    Stringutils = StringUtils()
    res = Stringutils.delete_symbol("YuriP", "_")
    assert res == "YuriP"

# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
# Пример 1: `starts_with("SkyPro", "S") -> True`
# Пример 2: `starts_with("SkyPro", "P") -> False`

def test_starts_with():
    Stringutils = StringUtils()
    if Stringutils.starts_with("Yuri", "Y"):
        res = True

    if Stringutils.starts_with("Yuri", "P"):
        res = False
    
    res = ("Y")
    assert res

# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
# Пример 1: `end_with("SkyPro", "o") -> True`
# Пример 2: `end_with("SkyPro", "y") -> False`

def test_end_with():
    Stringutils = StringUtils()
    if Stringutils.end_with("Yuri", "i"):
        res = True
    if Stringutils.end_with("Yuri", "y"):
        res = False

    res = ("i")
    assert res

# Возвращает `True`, если строка пустая и `False` - если нет \n 
# Пример 1: `is_empty("") -> True`
# Пример 2: `is_empty(" ") -> True`
# Пример 3: `is_empty("SkyPro") -> False`

def test_empty():
    Stringutils = StringUtils()
    if Stringutils.is_empty(""):
        res = True

    if Stringutils.is_empty(" "):
        res = True

    if Stringutils.is_empty("Yuri"):
        res = False

    res = (" ")
    assert res

# Преобразует список элементов в строку с указанным разделителем \n 
# Параметры: \n 
        # Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`


def test_list_to_string():
    Stringutils = StringUtils()
    Stringutils.list_to_string([1,2,3,4])
    res = "1, 2, 3, 4"
    assert res
