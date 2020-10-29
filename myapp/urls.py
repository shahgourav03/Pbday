from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('friends', views.friends, name='friends'),
    path('family', views.family, name='family'),
    path('lovelies', views.lovelies, name='lovelies'),
    path('found', views.searchFound, name='new_search'),
    path('<name>', views.detailView, name='detail')
]