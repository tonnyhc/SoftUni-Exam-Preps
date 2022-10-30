from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models



class Profile(models.Model):
    MAX_USERNAME_LEN = 10
    MIN_USERNAME_LEN = 2
    USERNAME_ERROR_MESSAGE = 'The username must be a minimum of 2 chars'

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=[
            validators.MinLengthValidator(MIN_USERNAME_LEN, message=USERNAME_ERROR_MESSAGE), ]
    )

    email = models.EmailField()
    age = models.IntegerField(
        validators=[validators.MinValueValidator(18)]
    )
    password = models.CharField(

        max_length=30
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True
    )



choices = (
    ("Sports Car", 'Sports Car'),
    ('Pickup', 'Pickup'),
    ('Crossover', 'Crossover'),
    ('Minibus', 'Minibus'),
    ('Other', 'Other')
)


def year_validator(value):
    if value < 1980 or value > 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Car(models.Model):
    MAX_TYPE_LEN = 10
    MAX_MODEL_LEN = 20
    MIN_MODEL_LEN = 2
    type = models.CharField(
        max_length=MAX_TYPE_LEN,
        choices=choices
    )
    model = models.CharField(
        max_length=MAX_MODEL_LEN,
        validators=[validators.MinLengthValidator(MIN_MODEL_LEN)]
    )
    year = models.IntegerField(
        validators=[year_validator]
    )
    image_url = models.URLField()
    price = models.FloatField(
        validators=[validators.MinValueValidator(1)]
    )
