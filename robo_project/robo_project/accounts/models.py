from django.core import validators
from django.contrib.auth import models as auth_models
from django.db import models

from robo_project.accounts.managers import AppUserManager
from robo_project.robots.models import AppRobots


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_CITY = 30
    MAX_LEN_ADDRESS = 50

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,

    )
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
        )
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
        )
    )
    city = models.CharField(
        max_length=MAX_LEN_CITY,
    )

    address = models.CharField(
        max_length=MAX_LEN_ADDRESS,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True,
    )
    username = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )


    # User credentials - email and password
    USERNAME_FIELD = 'email'
    objects = AppUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UserRobots(models.Model):
    user = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
    )

    robot_name = models.ForeignKey(
        AppRobots,
        on_delete=models.RESTRICT,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )
    user_robots_quantity = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
