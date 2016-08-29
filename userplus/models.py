from __future__ import unicode_literals
import datetime
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from userplus.lib.utils import hash_str


class UserPlus(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activation_key = models.CharField(max_length=400, blank=True, null=True)
    activation_expiry_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
        unique_together = ('email',)  # hack to make emails unique

    def save(self, *args, **kwargs):
        # coerce to lowercase for case insensitivity.
        if not self.pk:
            self.username = self.username.lower()
            self.email = self.email.lower()

        if 'set_activation_key' in kwargs and kwargs.pop('set_activation_key'):
            self.set_activation_key()
        super(UserPlus, self).save(*args, **kwargs)

    def set_activation_key(self):
        self.activation_key = hash_str(self.email, 5)
        activation_days = datetime.timedelta(days=getattr(settings, 'USERPLUS_ACTIVATION_DAYS', 2))
        self.activation_expiry_date = datetime.datetime.now() + activation_days
