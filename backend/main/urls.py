from django.urls import path
from .views import DeveloperView

urlpatterns = [
    path('dev/', DeveloperView.as_view(), name='dev')
]