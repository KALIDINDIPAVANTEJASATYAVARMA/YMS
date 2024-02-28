from django.contrib.auth.backends import BaseBackend
from .models import mktg_master

class MktgMasterBackend(BaseBackend):
    def authenticate(self, request, user_id=None, password=None):
        try:
            user = mktg_master.objects.get(user_id=user_id)
            if user.password == password:
                return user
        except mktg_master.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return mktg_master.objects.get(user_id=user_id)
        except mktg_master.DoesNotExist:
            return None