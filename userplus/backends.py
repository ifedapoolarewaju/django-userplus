from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class UserPlusBackend(ModelBackend):

    def authenticate(self, username=None, password=None, email=None, **kwargs):

        if email:
            UserModel = get_user_model()
            try:
                user = UserModel._default_manager.get(email=email)
                if not user.check_password(password):
                    user = None
            except UserModel.DoesNotExist:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a non-existing user (#20760).
                UserModel().set_password(password)
        else:
            user = super(UserPlusBackend, self).authenticate(
                username=username, password=password, **kwargs)

        if getattr(user, 'is_active', None):
            return user
