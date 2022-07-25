
from django.urls import path
from rent_a_port import views

urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index, name="home"),
    path('home', views.index, name="home"),
    path('about', views.about, name="about"),
    path('login', views.loginu, name="login"),
    path('logout', views.logoutu, name="login"),
    path('signup', views.signup, name="signup"),
    path('contacts', views.contactu, name="contacts"),
    path('about', views.about, name="about"),
    path('add', views.add_p, name="add"),
    path('propertys', views.propertys, name="propertys"),
    path('my_property', views.my_property, name="my_property"),
    path('profile', views.profile, name="profile"),
    # path('base', views.base, name="base"),
    path('del_property/<event_id>', views.del_property, name="del_property"),

    path('logout', views.logout, name="about")
]
