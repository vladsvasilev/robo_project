from django.core import validators
from django.db import models


class AppMassages(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_CITY = 30
    MAX_LEN_ADDRESS = 50

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    message = models.CharField(
        max_length=250,
        null=False,
        blank=False,

    )




