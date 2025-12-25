from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('profile', views.get_profile, name='profile'),
    path("create", views.create_user, name="create_user"),
]
