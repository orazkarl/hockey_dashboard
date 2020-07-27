from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    phone = models.CharField('Телефон', max_length=100)
    avatar = models.ImageField('Фото', upload_to='avatars')
    dob = models.DateField('Дата рожения', null=True)
    is_access = models.BooleanField('Доступ в тестирование', default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='file')
    title_file = models.CharField('Названия документа', max_length=150)
    file = models.FileField('Файл', null=True, blank=True, upload_to='docs')
    date_test = models.DateTimeField('Дата тестирования', null=True, blank=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документ'

    def __str__(self):
        return self.title_file
