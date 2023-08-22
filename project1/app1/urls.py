from django.urls import path
from . import views

urlpatterns = [
    path('', views.gitbucket, name='gitbucket'),
    path('home.html/repositories/', views.repositories_page, name='repositories'),
    path('home.html/project/', views.project_page, name='project'),
    path('signup.html/',views.signup,name='signup'),
    path('login.html/',views.login,name='login'),
    path('home.html/',views.homepage,name='home'),
    path('home.html/project/createproject/', views.createproject, name='createproject'),
    path('home.html/project/createproject/addproject/', views.addproject, name='addproject'),
    path('home.html/repositories/createrepositories/', views.createrepositories, name='createrepositories'),
    path('home.html/repositories/createrepositories/addrepositories/', views.addrepositories, name='addrepositories'),

]

