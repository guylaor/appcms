from django.conf import settings
from .models import UserProfile


class CustomUserAuth(object):

    def authenticate(self, email=None, password=None):
        try:
            user = UserProfile.objects.get(email=email)
            if UserProfile.check_password(user, password):
                # TODO: add saving timestamp of latest login
                # and Log of user login time and user agent
                return user
            else:
                # TODO: add here check for multiple login attempts
                # and locking of account after several unsuccsful login attempts
                return None
        except UserProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
