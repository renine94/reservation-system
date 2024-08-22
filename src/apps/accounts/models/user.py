from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

from src.core.base.model import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have a valid email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    회원 테이블
    """
    phone_number_validator = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')

    email = models.EmailField('이메일', unique=True)
    username = models.CharField('이름', max_length=30)
    phone_number = models.CharField('핸드폰 번호', validators=[phone_number_validator], max_length=11, blank=True, null=True)
    is_active = models.BooleanField('활성 유저 여부', default=True)
    is_staff = models.BooleanField('직원 여부', default=False)
    is_superuser = models.BooleanField('관리자 여부', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name_plural = verbose_name = '유저'
        indexes = [
            models.Index(fields=["email"], name="idx_email"),
        ]

    def __str__(self):
        return self.email
