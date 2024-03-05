from django.urls import path

from . import views

app_name = 'people'
urlpatterns = [
    path("", views.TeachersView.as_view(), name="teachers_list"),
    path("teacher/<int:pk>/", views.DetailTeacherView.as_view(), name="teacher_detail"),
]
