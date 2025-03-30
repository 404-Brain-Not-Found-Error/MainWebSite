import os
import django
from faker import Faker
from django.core.files import File
from random import choice, randint, sample
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from main.models import Developer, Project, ProjectImages, Service, Skills, Role, User

fake = Faker('ru_RU')

def create_skills():
    skills = ['Python', 'Django', 'JavaScript', 'React', 'HTML/CSS', 'SQL', 'Figma', 'Git']
    for skill in skills:
        Skills.objects.get_or_create(title=skill, slug=skill.lower())

def create_roles():
    roles = ['Backend', 'Frontend', 'Designer', 'Team Lead', 'DevOps']
    for role in roles:
        Role.objects.get_or_create(title=role, slug=role.lower())

def create_developers(num=5):
    skills = list(Skills.objects.all())
    roles = list(Role.objects.all())
    
    for _ in range(num):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='testpass123'
        )
        dev = Developer.objects.create(
            user=user,
            full_name=fake.name(),
            biography=fake.text(),
            role=choice(roles),
            github=f'https://github.com/{fake.user_name()}',
            telegram=f'@{fake.user_name()}'
        )
        dev.skills.set(sample(skills, randint(1, 3)))

def create_projects(num=3):
    developers = list(Developer.objects.all())
    skills = list(Skills.objects.all())
    
    for _ in range(num):
        project = Project.objects.create(
            title=fake.catch_phrase(),
            link=f'https://{fake.domain_name()}',
            description=fake.paragraph(),
            is_stock=choice([True, False])
        )
        project.developers.set(sample(developers, randint(1, 2)))
        project.skills.set(sample(skills, randint(2, 4)))

def create_services():
    services = [
        ('Веб-разработка', 'Создание сайтов любой сложности', 'от 50 000 ₽'),
        ('Дизайн', 'UI/UX дизайн для приложений', 'от 30 000 ₽'),
        ('Консультация', 'Техническая экспертиза проекта', 'от 5 000 ₽/час')
    ]
    for title, desc, price in services:
        Service.objects.create(title=title, description=desc, price=price)

def main():
    print('Создание навыков...')
    create_skills()
    print('Создание ролей...')
    create_roles()
    print('Создание разработчиков...')
    create_developers()
    print('Создание проектов...')
    create_projects()
    print('Создание услуг...')
    create_services()
    print('Готово! Данные созданы.')

if __name__ == '__main__':
    main()