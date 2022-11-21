from django.urls import path,include
from passApp import views

urlpatterns = [
    
    # path('', views.login),
    # path('login', views.login),
    path('', views.signup_views),
    path('handelLogin', views.handelLogin_views),
    path('logout', views.logout_view),
    path('handelSignup', views.handelSignup_views),

    path('entry', views.entry),
    path('show', views.show),
    path('send', views.send),
    path('delete', views.delete),
    path('edit', views.edit),
    path('editRecord', views.editRecord),
    
]