from django.shortcuts import render

user = [
    {'id': 0, 'name': 'Valentyn', 'age': 19},
    {'id': 1, 'name': 'Maria', 'age': 20}
]
def show_user(request):
    return render(request, 'user.html', {'user': user})



def new_user(request, name, age, id):
    user.append({'id': id, 'name': name, 'age': age})
    return render(request, 'user.html', {'user': user})

def delete_user(request, id_user):
    for i in user:
        if i.id == id_user:
            del i
    return render(request, 'user.html', {'user': user})
