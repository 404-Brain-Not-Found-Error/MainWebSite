from django.db import models
from django.contrib.auth.models import User

class Developer(models.Model):
    user = models.OneToOneField(User, verbose_name='Разработчик', on_delete=models.CASCADE)
    full_name = models.CharField('ФИО', max_length=300)
    biography = models.TextField('Биография')
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, blank=True, null=True)
    entry_date = models.DateTimeField('Дата вступления', auto_now_add=True)
    is_stock = models.BooleanField('Показать?', default=False)

    def __str__(self):
        return f'User{self.user.name}, full name: {self.full_name}'
    
    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural ='Разработчики'


class Skills(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Умение'
        verbose_name_plural ='Умения'


class Role(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural ='Роли'

class ProjectImages(models.Model):
    image = models.ImageField(upload_to='project/image/%Y/%m/%d/', height_field=None, width_field=None, max_length=None)
    is_stock = models.BooleanField('Показать?', default=False)

    def __str__(self):
        return f'{self.image}'
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural ='Изображения'

    
class Project(models.Model):
    title = models.CharField('Название', max_length=100)
    link = models.CharField('Ссылка', max_length=1000)
    description = models.TextField()
    images = models.ManyToManyField(ProjectImages, verbose_name='Изображения')
    developers = models.ManyToManyField(Developer, verbose_name='Разработчики')
    is_stock = models.BooleanField('Показать?', default=False)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural ='Проекты'


class Service(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField()
    price = models.CharField('Цена', max_length=100)
    
    def __str__(self):
        return f'{self.image}'
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural ='Услуги'
