from django.urls import path
from . import views

urlpatterns = [
    path('student/list/', views.student_list, name='student_list'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/update/<int:student_id>/', views.student_update, name='student_update'),
    path('class/list/', views.class_list, name='class_list'),
    path('class/add/', views.class_add, name='class_add'),
    path('class/update/<int:class_id>/', views.class_update, name='class_update'),
]