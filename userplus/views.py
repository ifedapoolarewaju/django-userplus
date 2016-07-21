from django.utils import timezone

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect


def confirm_registration(request, activation_key):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    user = get_object_or_404(get_user_model(), activation_key=activation_key, is_active=False)

    if timezone.now() < user.activation_expiry_date:
        user.is_active = True
        user.activation_expiry_date = timezone.now()
        user.save()
        user.email_user('Account Activation', 'Your account has been activated')
    # dont send message if key is expired to avoid verbose message to hackers
    return HttpResponseRedirect(reverse('signin'))
