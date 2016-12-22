from django.db import models
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

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'


    
