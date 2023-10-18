"""
Module docstring
"""


def multiplier(number: float) -> float:
    """
    Multiplies argument number by 2
    :param number: numeric value
    :return: multiplied value
    """
    return number * 2


# Google docstring format
def multiplier_3(number: float) -> float:
    """
    Multiplies argument number by 3
    Args:
        number: numeric value
    Returns: multiplied value
    """
    return number * 3


print(multiplier.__doc__)
print(multiplier_3.__doc__)

# Aby wygenerować dokumentację tego pliku w postaci html: python -m pydoc -w 2_docs
# Ewentualnie: pdoc3 --html 2_docs (wymaga instalacji: pip install pdoc3)
