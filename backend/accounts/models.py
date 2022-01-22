from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


def contain_blank(value):
    if ' ' in value:
        raise ValidationError('공백이 포함될 수 없습니다.')

class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=20, validators=[MinLengthValidator(3),
                                                                             contain_blank])