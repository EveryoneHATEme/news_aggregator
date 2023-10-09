import re
from num2words import num2words


def remove_except_letters(text: str) -> str:
    return re.sub(r"[^a-zA-Zа-яА-Я\s]", " ", text)


def replace_numbers(text: str) -> str:
    def replacer(match):
        str_representation = match.group(0)
        if len(str_representation) > 11:
            return str_representation
        number = int(str_representation)
        return num2words(number, lang="ru")

    return re.sub(r"\d+", replacer, text)


def remove_multiple_spaces(text: str) -> str:
    return re.sub("\s+", " ", text).strip()


def remove_links(text: str) -> str:
    return re.sub(r"https?://\S+|www\.\S+", " ", text)


def preprocess_text(text: str) -> str:
    func_list = [
        str,
        str.lower,
        remove_links,
        replace_numbers,
        remove_except_letters,
        remove_multiple_spaces,
    ]
    for func in func_list:
        text = func(text)
    return text
