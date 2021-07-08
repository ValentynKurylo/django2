from django.shortcuts import render

user = [
    {'name': 'Valentyn', 'age': 19}
]


def show_user(request):
    return render(request, 'user.html', {'user': user})


def new_user(request, name, age):
    user.append({'name': name, 'age': age})
    return render(request, 'user.html', {'user': user})
