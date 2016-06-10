import re

from django.core.exceptions import ValidationError


def username_pattern(value):
    pattern = re.compile(r'^([\w\-\_@.]+)')
    if not pattern.match(value) or pattern.match(value).groups()[0] != value:
        raise ValidationError('"%s" is not a valid username. Spaces are not allowed.' % value)


def password_pattern(value):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&.])[A-Za-z\d$@$!%*?&.]{8,}')
    if not pattern.match(value):
        raise ValidationError(
            'Must contain 8 characters, Uppercase and Lowercase Alphabet, Number and Special Character')
