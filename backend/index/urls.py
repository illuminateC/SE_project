from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from index import views

app_name = 'index'



urlpatterns = [
    path('video/', views.video),
    path('user/',views.user),
    path('getfollow/',views.getfollow),
    path('getzone/',views.getzone),
    path('id2name/',views.id2name),
    path('isfollowed/',views.isfollowed),
    path('getrecommand/',views.getrecommand),
]