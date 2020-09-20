import random
import string



class Generator(object):

    @staticmethod
    def random_string_generator(length: int, lowercase: bool = True, uppercase: bool = True, punctuation: bool = True,
                                digits: bool = True, separator: str = "") -> str:
        characters = ""
        if lowercase:
            characters += string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
        if punctuation:
            characters += string.punctuation
        if digits:
            characters += string.digits

        return separator.join([
            random.choice(
                characters
            ) for _ in range(length)
        ])
