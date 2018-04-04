from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('signup', views.signup, name = "user_signup"),
    path('login', views.user_login, name = "user_login"),
    path('logout', views.user_logout, name = "logout"),
    re_path(r'^home/(?P<name>\w+([.| ]\w+)*)/', views.user_home, name = "user_home_page"),
    re_path(r'^history/(?P<name>\w+([.| ]\w+)*)/', views.user_history, name = "user_history"),
    re_path(r'', views.index, name = "proj_index"),
]
