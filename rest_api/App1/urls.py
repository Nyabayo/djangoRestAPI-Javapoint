from django.urls import path
from .views import StudentView

urlpatterns = [
    path('basic', StudentView.as_view())
]
