from django.urls import path
from .views import show_user, new_user, delete_user

urlpatterns = [
    path('', show_user),
    path('/create/<str:name>/<int:age>/<int:id>', new_user),
    path('/delete/<int:id_user>', delete_user)
]