from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>', views.studentDetailsView),

    path('employee/',views.EmployeeView.as_view()),
    path('employee/<int:pk>/',views.EmployeeDetailsView.as_view()),
]