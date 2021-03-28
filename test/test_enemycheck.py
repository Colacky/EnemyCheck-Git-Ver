import pytest
from enemycheck import get_data, fill_data, format_realm, translate_cyrillic, cyrillic_translit


def test_translate_cyrillic_true():
    assert translate_cyrillic('Гордунни', cyrillic_translit) == 'Gordunni'


def test_translate_cyrillic_false():
    assert translate_cyrillic('Boulderfist', cyrillic_translit) == 'Boulderfist'


if __name__ == "__main__":
    test_translate_cyrillic_true()
    test_translate_cyrillic_false()
