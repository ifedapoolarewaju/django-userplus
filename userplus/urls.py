from django.conf.urls import url
from userplus import views

urlpatterns = [url(r'^confirm/(?P<activation_key>\w+)/',
                   views.confirm_registration, name='userplus_confirm_registration'), ]
