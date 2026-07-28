from app.utils.funcoes import validar_ano


def test_validar_ano_valido():
    assert validar_ano(2024) is True


def test_validar_ano_invalido():
    assert validar_ano(1800) is False


def test_validar_ano_texto():
    assert validar_ano("2023") is True
