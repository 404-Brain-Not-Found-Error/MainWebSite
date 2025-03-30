from django.db import models
from django.contrib.auth.models import User

class Developer(models.Model):
    user = models.OneToOneField(User, verbose_name='Разработчик', on_delete=models.CASCADE)
    full_name = models.CharField('ФИО', max_length=300)
    biography = models.TextField('Биография')
    github = models.URLField('GitHub', blank=True)
    telegram = models.CharField('Telegram', max_length=50, blank=True)
    avatar = models.ImageField('Аватар', upload_to='developers/avatars/', blank=True)
    skills = models.ManyToManyField('Skills', verbose_name='Навыки', blank=True)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, blank=True, null=True)
    entry_date = models.DateTimeField('Дата вступления', auto_now_add=True)
    is_stock = models.BooleanField('Показать?', default=False)

    def __str__(self):
        return f'User{self.user}, full name: {self.full_name}'
    
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


class Project(models.Model):
    title = models.CharField('Название', max_length=100)
    link = models.CharField('Ссылка', max_length=1000)
    description = models.TextField()
    repository_url = models.URLField('Репозиторий', blank=True)
    demo_url = models.URLField('Демо', blank=True)
    start_date = models.DateField('Дата начала', null=True, blank=True)
    end_date = models.DateField('Дата завершения', null=True, blank=True)
    developers = models.ManyToManyField(Developer, verbose_name='Разработчики')
    skills = models.ManyToManyField(Skills, verbose_name='Необходимые навыки', blank=True)
    roles_needed = models.ManyToManyField(Role, verbose_name='Требуемые роли', blank=True)
    is_stock = models.BooleanField('Показать?', default=False)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural ='Проекты'

class ProjectStage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='stages')
    title = models.CharField('Этап', max_length=200)
    description = models.TextField('Описание', blank=True)
    is_completed = models.BooleanField('Завершён', default=False)
    deadline = models.DateField('Дедлайн', null=True, blank=True)

    def __str__(self):
        return f'{self.project.title} - {self.title}'

    class Meta:
        verbose_name = 'Этап проекта'
        verbose_name_plural = 'Этапы проекта'


class ProjectImages(models.Model):
    image = models.ImageField(upload_to='project/image/%Y/%m/%d/', height_field=None, width_field=None, max_length=None)
    is_stock = models.BooleanField('Показать?', default=False)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    alt_text = models.CharField('Описание изображения', max_length=200, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.image}'
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural ='Изображения'

class Testimonial(models.Model):
    client_name = models.CharField('Имя клиента', max_length=100)
    client_role = models.CharField('Должность/компания', max_length=100, blank=True)
    text = models.TextField('Текст отзыва')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Проект')
    rating = models.PositiveSmallIntegerField('Оценка (1-5)', default=5)
    is_approved = models.BooleanField('Одобрено', default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Technology(models.Model):
    name = models.CharField('Название', max_length=100)
    icon = models.CharField('Иконка (Font Awesome класс)', max_length=50, blank=True)
    projects = models.ManyToManyField(Project, related_name='technologies', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'

class Service(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField()
    developers = models.ManyToManyField(Developer, verbose_name='Ответственные', blank=True)
    duration = models.CharField('Срок выполнения', max_length=100, blank=True)
    is_active = models.BooleanField('Активна?', default=True)
    price = models.CharField('Цена', max_length=100)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural ='Услуги'


class BlogPost(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField('Содержание')
    author = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=False)
    tags = models.ManyToManyField('Tag', verbose_name='Теги', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Tag(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    color = models.CharField('Цвет (HEX)', max_length=7, default='#000000')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField('Имя автора', max_length=100)
    author_email = models.EmailField('Email автора', blank=True)
    text = models.TextField('Текст комментария')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'