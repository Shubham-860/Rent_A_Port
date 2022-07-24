
from django.urls import path
from rent_a_port import views

urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index, name="home"),
    path('about', views.about, name="about"),
    path('login', views.loginu, name="login"),
    path('logout', views.logoutu, name="login"),
    path('signup', views.signup, name="signup"),
    path('contacts', views.contactu, name="contacts"),
    path('about', views.about, name="about"),
    path('add', views.add_p, name="add"),
    path('propertys', views.propertys, name="propertys"),
    # path('base', views.base, name="base"),

    path('logout', views.logout, name="about")
]
