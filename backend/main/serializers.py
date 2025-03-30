from rest_framework import serializers
from .models import Developer, Project, ProjectImages, Service, Skills, Role, BlogPost
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    skills = SkillsSerializer(many=True, read_only=True)
    role = RoleSerializer(read_only=True)
    
    class Meta:
        model = Developer
        fields = '__all__'
        depth = 1

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = ['id', 'image', 'alt_text', 'order']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    developers = DeveloperSerializer(many=True, read_only=True)
    skills = SkillsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'
        lookup_field = 'slug'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    author = DeveloperSerializer(read_only=True)
    
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'