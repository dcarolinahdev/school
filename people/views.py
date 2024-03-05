from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.http import HttpResponse

from .models import Teacher, Student


class TeachersView(generic.ListView):
    template_name = 'people/teachers_list.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teacher.objects.order_by('last_name')
    
class DetailTeacherView(generic.DetailView):
    model = Teacher
    template_name = 'people/teacher_detail.html'

    def get_queryset(self):
        """
        """
        return Teacher.objects.all()


