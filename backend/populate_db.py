import os
import django
from faker import Faker
from django.core.management import call_command
from django.core.files import File
from random import choice, randint, sample
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Developer, Project, ProjectImages, Service, Skills, Role

fake = Faker('ru_RU')

def create_superuser():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )

def create_skills():
    skills = [
        'Python', 'Django', 'DRF', 'Flask',
        'JavaScript', 'TypeScript', 'React', 'Vue',
        'PostgreSQL', 'MongoDB', 'Docker', 'Kubernetes',
        'AWS', 'Git', 'CI/CD', 'GraphQL'
    ]
    return [Skills.objects.get_or_create(title=skill, slug=skill.lower())[0] for skill in skills]

def create_roles():
    roles = [
        'Backend Developer', 'Frontend Developer', 
        'Fullstack Developer', 'DevOps Engineer',
        'UI/UX Designer', 'Team Lead', 'QA Engineer'
    ]
    return [Role.objects.get_or_create(title=role, slug=role.lower())[0] for role in roles]

def create_developers(num=10):
    skills = Skills.objects.all()
    roles = Role.objects.all()
    
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
            telegram=f'@{fake.user_name()}',
            entry_date=fake.date_between(start_date='-2y', end_date='today')
        )
        dev.skills.set(sample(list(skills), randint(2, 5)))

def create_projects():
    developers = list(Developer.objects.all())
    skills = list(Skills.objects.all())
    
    projects = [
        {
            "title": "Корпоративный портал",
            "description": "Внутренняя система для управления бизнес-процессами",
            "skills": ["Python", "Django", "PostgreSQL", "Docker"]
        },
        {
            "title": "Мобильное приложение для трекинга здоровья",
            "description": "Приложение для мониторинга физической активности",
            "skills": ["JavaScript", "React", "TypeScript"]
        },
        {
            "title": "Образовательная платформа",
            "description": "Онлайн-курсы с системой проверки заданий",
            "skills": ["Python", "Django", "JavaScript", "Vue"]
        },
        {
            "title": "Агрегатор новостей",
            "description": "Платформа для сбора новостей из различных источников",
            "skills": ["Python", "Flask", "JavaScript"]
        },
        {
            "title": "Система бронирования отелей",
            "description": "Поиск и бронирование отелей по всему миру",
            "skills": ["Python", "Django", "React", "PostgreSQL"]
        },
        {
            "title": "Фитнес-трекер с AI",
            "description": "Персонализированные тренировки с ИИ",
            "skills": ["JavaScript", "React", "TypeScript"]
        }
    ]
    
    for project_data in projects:
        project = Project.objects.create(
            title=project_data["title"],
            link=f"https://{fake.domain_name()}",
            description=project_data["description"],
            is_stock=fake.boolean(chance_of_getting_true=80)
        )
        project.developers.set(sample(developers, randint(1, 3)))
        project.skills.set([s for s in skills if s.title in project_data["skills"]])

def create_services():
    services = [
        {"title": "Веб-разработка", "price": "от 50 000 ₽", "duration": "2-4 недели"},
        {"title": "Мобильная разработка", "price": "от 80 000 ₽", "duration": "4-6 недель"},
        {"title": "UI/UX дизайн", "price": "от 30 000 ₽", "duration": "1-2 недели"},
        {"title": "Технический аудит", "price": "от 20 000 ₽", "duration": "1 неделя"}
    ]
    
    for service in services:
        Service.objects.create(
            title=service["title"],
            description=fake.paragraph(),
            price=service["price"],
            duration=service["duration"]
        )

def main():
    print("Очистка базы данных...")
    call_command('flush', '--noinput')
    
    print("Создание суперпользователя...")
    create_superuser()
    
    print("Создание навыков...")
    create_skills()
    
    print("Создание ролей...")
    create_roles()
    
    print("Создание разработчиков...")
    create_developers(8)  # 8 разработчиков
    
    print("Создание проектов...")
    create_projects()
    
    print("Создание услуг...")
    create_services()
    
    print("Готово! Данные успешно созданы.")

if __name__ == '__main__':
    main()