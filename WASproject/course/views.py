from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Courses

# Create your views here.


def course(request):
    course_list = Courses.objects.order_by('startDate')

    context_dict = {}
    context_dict['courses'] = course_list

    return render(request, 'course/course.html', context=context_dict)
