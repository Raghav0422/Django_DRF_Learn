from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename="emplo")

urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>', views.studentDetailsView),

    path('employee/',views.EmployeeView.as_view()),
    path('employee/<int:pk>/',views.EmployeeDetailsView.as_view()),

    path('',include(router.urls))
]