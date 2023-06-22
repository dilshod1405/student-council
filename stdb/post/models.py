from django.db import models

from user.models import User
from user.validations import post_validator, validate_file


class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = 'Post kategoriyasi'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='Fayl nomi')
    is_created = models.DateField(auto_now=True, verbose_name='Yuklangan vaqti')
    file = models.FileField(validators=[post_validator, validate_file],
                            help_text='Faylning maksimal hajmi 20Mb bo`lishi lozim!',
                            upload_to='media/posts', blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    owner_comment = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Izoh egasi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Fayl kategoriyasi')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Post muallifi',
                               related_name='author_post')

    class Meta:
        db_table = 'Postlar'

    def __str__(self):
        return self.title
