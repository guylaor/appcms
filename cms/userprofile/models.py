from django.db import models
from datetime import date
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserProfileManager(BaseUserManager):

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have email address')

        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email',
        max_length = 255,
        unique=True
    )
    is_locked = models.BooleanField(default=False)
    email_validated = models.BooleanField(default=False)
    require_pass_change = models.BooleanField(default=False)
    pass_last_changed = models.DateField(default=date.today)
    validation_hash = models.CharField(max_length=255, null=True)
    secondary_email = models.EmailField(max_length=255, null=True)
    sms_number = models.CharField(max_length=50, null=True)
    recent_login_attempts = models.TextField(null=True)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
