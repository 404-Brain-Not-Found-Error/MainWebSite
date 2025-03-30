from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'developers', views.DeveloperViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'blog', views.BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('', include(router.urls)),
]