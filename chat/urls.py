from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_view.LoginView.as_view(template_name='chat/signin.html'), name='signin'),
    path('signout/', auth_view.LogoutView.as_view(), name='signout'),
    path('room/<uuid:pk>/', views.room, name='room'),
    path('room/create/', views.create_room, name='create_room'),
    path('room/edit/<uuid:pk>/', views.edit_room, name='edit_room'),
    path('room/delete/<uuid:pk>/', views.delete_room, name='delete_room'),
]
