from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field import modelfields

from user.validations import validate_image, custom_validator


class Universities(models.Model):
    title = models.CharField(max_length=100, verbose_name='Oliy ta`lim muassasi')

    class Meta:
        db_table = 'Universitetlar'

    def __str__(self):
        return self.title


class District(models.Model):
    district = models.CharField(max_length=50, verbose_name='Tuman')

    class Meta:
        db_table = 'Tumanlar'

    def __str__(self):
        return self.district


class Region(models.Model):
    region = models.CharField(max_length=50, verbose_name='Viloyat')

    class Meta:
        db_table = 'Hududlar'

    def __str__(self):
        return self.region


class User(AbstractUser):
    phone = modelfields.PhoneNumberField(unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, verbose_name='Viloyat', blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, verbose_name='Tuman', blank=True)
    profile_photo = models.ImageField(validators=[validate_image, custom_validator], verbose_name='Profil rasmi')
    telegram_username = models.CharField(max_length=100, null=True, verbose_name='Telegram username', blank=True)
    instagram_username = models.CharField(max_length=20, null=True, verbose_name='Instagram username', blank=True)
    facebook_username = models.CharField(max_length=50, verbose_name='Facebook username', blank=True)
    about = models.TextField(max_length=1000, verbose_name='Qisqacha ma`lumot', blank=True, null=True)
    university = models.ForeignKey(Universities, on_delete=models.CASCADE, null=True,
                                   verbose_name='O`qish joyi',
                                   blank=True)
    course = models.PositiveIntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)],
                                         default=0, verbose_name='Bosqich', blank=True)

    class Meta:
        db_table = 'Foydalanuvchilar'

    def __str__(self):
        return self.username
