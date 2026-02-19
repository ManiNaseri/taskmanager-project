from django.urls import path
from .views import Rest

urlpatterns = [
    path("rest/", Rest.as_view()),
]
