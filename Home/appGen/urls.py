from django.contrib import admin
from django.urls import path, include
from appGen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('instructors', views.instructors, name='instructors'),
    path('delete-instructors/<str:pk>/', views.delInstructors, name = 'delInstructors'),
    path('timeslots', views.timeslots, name='timeslots'),
    path('delete-timeslots/<str:pk>/', views.deltimeslots, name = 'deltimeslots'),
    path('rooms', views.rooms, name='rooms'),
    path('delete-rooms/<str:pk>/', views.delrooms, name = 'delrooms'),
    path('programmes', views.programmes, name='programmes'),
    path('delete-programmes/<str:pk>/', views.delprogrammes, name = 'delprogrammes'),
    path('courses', views.courses, name='courses'),
    path('sections', views.sections, name='sections'),
]
    