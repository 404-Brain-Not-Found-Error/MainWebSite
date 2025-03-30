from rest_framework import viewsets, permissions, filters
from .models import Developer, Project, Service, BlogPost
from .serializers import (
    DeveloperSerializer,
    ProjectSerializer,
    ServiceSerializer,
    BlogPostSerializer
)
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from django.views import View
from rest_framework.reverse import reverse_lazy

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        api_links = {
            'developers': reverse_lazy('developer-list'),
            'projects': reverse_lazy('project-list'),
            'services': reverse_lazy('service-list'),
            'blog': reverse_lazy('blogpost-list'),
            'admin': reverse_lazy('admin:index')
        }
        
        context = {
            'title': '404 Brain Not Found',
            'description': 'Перспективная команда разработчиков',
            'api_links': api_links
        }
        return render(request, self.template_name, context)

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.filter(is_stock=True)
    serializer_class = DeveloperSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['full_name', 'biography']
    filterset_fields = ['role']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_stock=True)
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['developers', 'skills']

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['author', 'tags']

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.query_params.get('tag')
        if tag:
            queryset = queryset.filter(tags__name=tag)
        return queryset