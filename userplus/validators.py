import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class PatternValidator(object):
    error_message = ('Password Must contain Uppercase and Lowercase Alphabet,'
                     ' Number and Special Character.')

    def validate(self, password, user=None):
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&.])')
        if not pattern.match(password):
            raise ValidationError(_(self.error_message), code='password_too_weak')

    def get_help_text(self):
        return _(self.error_message)
