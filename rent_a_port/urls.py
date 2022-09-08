from django.contrib.auth import views as auth_views
from django.urls import path
from rent_a_port import views
urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index, name="home"),
    path('home', views.index, name="home"),
    path('about', views.about, name="about"),
    path('login', views.loginu, name="login"),
    path('login/<url>/', views.loginu, name="login"),
    path('logout', views.logoutu, name="login"),
    path('signup', views.signup, name="signup"),
    path('contacts', views.contactu, name="contacts"),
    path('about', views.about, name="about"),
    path('add', views.add_p, name="add"),
    path('propertys', views.propertys, name="propertys"),
    path('my_property', views.my_property, name="my_property"),
    path('profile', views.profile, name="profile"),
    path('profile_update', views.profile_update, name="profile_update"),

    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name="change_password/"),

    # temp
    path('contactInfoMail/<pid>/<abcd>', views.rough, name="contactInfoMail"),



    # path('base', views.base, name="base"),
    path('del_property/<Property_id>', views.del_property, name="del_property"),

    path('logout', views.logout, name="about"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),

]


