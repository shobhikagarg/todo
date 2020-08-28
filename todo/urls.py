from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="list"),
    path('update/<str:pk>/', views.updateTodo, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='about'),
    ]