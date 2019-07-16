from django.db import models
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist

from user.models import User


class Otp(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=False)
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OtpBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, errors=[]):
        if username.isdigit() and len(username) == 10:
            try:
                user = User.objects.get(phone=username)
            except:
                errors.append("Wrong phone number.")
                return

            try:
                otp = Otp.objects.get(
                    user=user, otp=password, used=False)
                otp.used = True
                otp.save()
                return otp.user
            except ObjectDoesNotExist:
                return
