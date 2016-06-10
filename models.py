from __future__ import unicode_literals
import datetime
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

from userplus.validators import password_pattern


class UserPlus(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activation_key = models.CharField(max_length=400, blank=True)
    activation_expiry_date = models.DateTimeField()

    class Meta:
        abstract = True
        unique_together = ('email',)  # hack to make emails unique

    def save(self, *args, **kwargs):
        self.set_activation_expiry()
        super(UserPlus, self).save(*args, **kwargs)

    def set_activation_expiry(self):
        if self.activation_key:
            UserModel = get_user_model()
            try:
                instance = UserModel.objects.get(username=self.username)
            except UserModel.DoesNotExist:
                instance = None
            if not instance or self.activation_key != instance.activation_key:
                self.activation_expiry_date = datetime.datetime.now() + datetime.timedelta(days=2)


UserPlus._meta.get_field('password').validators = [password_pattern]
