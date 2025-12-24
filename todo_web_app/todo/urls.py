from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('list/', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:todo_id>/', views.todo_update, name='todo_update'),
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]