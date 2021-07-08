from django.urls import path
from .views import show_user, new_user

urlpatterns = [
    path('', show_user),
    path('/create/<str:name>/<int:age>', new_user)
]