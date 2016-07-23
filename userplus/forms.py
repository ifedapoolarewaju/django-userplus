import re

from django import forms
from django.contrib.auth import get_user_model

from userplus.lib.utils import hash_str


class SignUpForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        if commit:
            user.activation_key = hash_str(user.email, 5)
            user.save()
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
