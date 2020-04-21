from django.urls import path
from . import views

urlpatterns = [
    path('', views.userlogin, name='login' ),
    path('professor/', views.index, name='index' ),
    path('events/', views.events, name='events' ),
    path('student/', views.student, name='student' ),
    path('deadline/', views.deadline, name='deadline' ),
    path('create/', views.create, name='create' ),
    path('add_coursework/', views.add_book, name='add_coursework' ),
    path('student_add/', views.student_add, name='student_add' ),
    path('studentAdd/', views.studentAdd, name='studentAdd' ),
   
    path('edit/<id>/', views.edit, name='edit' ),
    path('add_color/<id>/', views.editColor, name='add_color' ),
    path('edit_task/<id>/', views.edit_task, name='edit_task' ),
    path('update/<id>/', views.update, name='update' ),
    path('updateColor/<id>/', views.updateColor, name='updateColor' ),
    path('updateTask/<id>/', views.updateTask, name='updateTask' ),
    path('calendar/', views.calendar, name='calendar'),
]
