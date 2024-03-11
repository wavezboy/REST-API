from django.urls import path
from Employee import views




urlpatterns = [
    path('department/', views.deparmentApi),
    path('department/<int:id>/', views.deparmentApi),
    path('employee/', views.employeeApi),
    path('employee/<int:id>', views.employeeApi)
]