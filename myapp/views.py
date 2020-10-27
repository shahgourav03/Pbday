import base64
from django.shortcuts import render
from .models import Friends, Family, Lovelies
import playsound
# import pygame
import subprocess


# Create your views here.

def home(request):
    # playsound.playsound('myapp/static/myapp/media/H2.mp3', True)
    return render(request, "myapp/home.html")


def new_search(request):
    print("hereeee")
    search = request.POST.get('hahaha')
    print(search)
    stuff_for_frontend = {
        'search': search
    }
    return render(request, "myapp/new_search.html", stuff_for_frontend)


def friends(request):
    model = Friends
    friendsData = []

    for f in Friends.objects.all():
        a = f.image
        friendsData.append((f.name, a.url[7:], f.message))

    stuff_to_frontend = {
        'friends': friendsData,
    }
    return render(request, "myapp/friends.html", stuff_to_frontend)


def family(request):
    model = Family
    familyData = []

    for f in Family.objects.all():
        a = f.image
        familyData.append((f.name, a.url[7:], f.message))
    stuff_to_frontend = {
        'family': familyData,
    }
    return render(request, "myapp/family.html", stuff_to_frontend)


def lovelies(request):
    model = Lovelies
    loveliesData = []

    for l in Lovelies.objects.all():
        a = l.image
        loveliesData.append((l.name, a.url[7:], l.message))

    stuff_to_frontend = {
        'lovelies': loveliesData,
    }
    return render(request, "myapp/lovelies.html", stuff_to_frontend)


def detailView(request, name):
    data = []

    if Friends.objects.filter(name=name):
        data = (Friends.objects.get(name=name))
    elif Family.objects.filter(name=name):
        data = (Family.objects.get(name=name))
    elif Lovelies.objects.filter(name=name):
        data = (Lovelies.objects.get(name=name))

    if data != []:
        # if True:
        message = data.message
        image_path = data.image.url[1:]
    else:
        message = "................."
        image_path = ('myapp/static/myapp/images/main.png')
        # image_path = ('/home/pi/PythonProg/Pbday/myapp/static/myapp/images/main.png')

    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    detail = {
        'name': name,
        'photo': image_data,
        'message': message
    }

    return render(request, "myapp/detail.html", detail)
