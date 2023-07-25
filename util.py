import random

chars = {
    'all': [chr(i) for i in range(33, 127)],
    'numbers': [chr(i) for i in range(48, 58)],
    'letters': [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)],
    'upper_case': [chr(i) for i in range(65, 91)],
    'lower_case': [chr(i) for i in range(97, 123)],

    # ascii punctuation codes excluding double quotes and backslashes (so as to not fuck up json strings)
    'punctuation': [chr(33)] + [chr(i) for i in range(35, 47)] + [chr(i) for i in range(58, 64)] + [chr(91)] + [chr(i) for i in range(93, 96)] + [chr(i) for i in range(123, 126)]
}


def random_string(length=14):
    return ''.join(random.choice(chars["letters"] + chars["numbers"] + chars["punctuation"]) for i in range(length))


def random_alphanumeric(length=18):
    return ''.join(random.choice(chars['letters'] + chars["numbers"]) for i in range(length))
