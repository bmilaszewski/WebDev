from django.urls import path
from .views import home, login_view, adminHome, createUser, hours, delete_teaching_assistant
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("adminHome/", adminHome, name="adminHome"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', success_url='admin/'), name='login'),
    path("createUser/", createUser, name='createUser'),
    path("hours/", hours, name="hours"),
    path('delete/<int:pk>/', delete_teaching_assistant, name='delete_teaching_assistant'),
]
