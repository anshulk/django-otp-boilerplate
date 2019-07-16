from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, password):
        user = self.model(phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(phone, password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    phone_validator = RegexValidator(
        regex='^\d{10}$', message="Invalid phone number")
    alpha = RegexValidator(
        r'^[a-zA-Z ]{5,100}$', 'Only letters and spaces are allowed in the name, min 5 characters')

    phone = models.CharField(unique=True, validators=[
                             phone_validator], max_length=10)
    name = models.CharField(
        validators=[alpha], max_length=100, blank=True, null=True)
    email = models.CharField(
        validators=[EmailValidator], max_length=500, blank=True, null=True)
    picture = models.ImageField(upload_to='users/pictures/',blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    objects = UserManager()

    class Meta:
        db_table = 'user'

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm):
        return True
