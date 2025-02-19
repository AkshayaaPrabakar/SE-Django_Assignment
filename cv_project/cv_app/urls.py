from django.urls import path # type: ignore
from .views import resume_view

urlpatterns = [
    path('resume/', resume_view, name='resume'),
]