from django.urls import path  # type: ignore
from .views import resume_view

urlpatterns = [
    path('', resume_view, name='home'),  # Set this as the default route
    path('resume/', resume_view, name='resume'),
]
