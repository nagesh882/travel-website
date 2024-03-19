from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class AccountManager(UserManager):
    def create_user(self, username, email_id, password=None):
        if not email_id:
            raise ValueError('Enter valid email address')

        UserData = self.model(
            username = username,
            email_id = self.normalize_email(email_id)
        )

        UserData.set_password(password)
        UserData.save(using = self._db)

        return UserData

    def create_superuser(self, username, email_id, password):
        
        UserData = self.create_user(
            username = username,
            email_id = self.normalize_email(email_id),
            password = password
        )

        UserData.is_admin = True
        UserData.is_active = True
        UserData.is_staff = True
        UserData.is_superuser = True

        UserData.save(using = self._db)

        return UserData


class Account(AbstractBaseUser):
    username = None

    username = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email_id'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    objects = AccountManager()