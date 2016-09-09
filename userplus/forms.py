import re

from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings


class SignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        kwargs = {'set_activation_key': getattr(settings, 'USERPLUS_SET_ACTIVATION_KEY')}
        user.is_active = not kwargs['set_activation_key']
        if commit:
            user.save(**kwargs)
        return user


class SignInForm(forms.Form):
    username_or_email = forms.CharField(
        label='Enter your username or email', max_length=70)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username_or_email(self):
        user_id = self.cleaned_data.pop('username_or_email')

        if re.match(r"[^@]+@[^@]+\.[^@]+", user_id):
            self.cleaned_data['email'] = user_id
        else:
            self.cleaned_data['username'] = user_id
