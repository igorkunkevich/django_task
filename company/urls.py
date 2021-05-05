from django.urls import path
from . import views

urlpatterns = [
    path("company/all", views.EmployeeListView.as_view()),
]
