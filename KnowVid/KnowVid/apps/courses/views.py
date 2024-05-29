from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.postgres.search import SearchVector
from django import forms

from .models import Course, Lesson, User
ITEMS_PER_PAGE = 4


@login_required
def course_list(request):
    order_value = request.GET.get('order')
    if order_value not in ['title', 'level', 'subject']:
        order_value = 'title'
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(
            title__icontains=query
        ).order_by(order_value) | Course.objects.filter(
            subject__icontains=query
        ).order_by(order_value) | Course.objects.filter(
            level__icontains=query
        ).order_by(order_value)
    else:
        courses = Course.objects.all().order_by(order_value)
    paginator = Paginator(courses, ITEMS_PER_PAGE)
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    return render(request, 'course/list.html', {'page': page, 'courses': courses})


@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    return render(request, 'course/details.html', {'course': course, 'lessons': lessons})


@login_required
def course_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        level = request.POST.get('level')
        subject = request.POST.get('subject')
        user = request.user 
        
        if title and level and subject and user:
            course = Course(title=title, level=level, subject=subject, user=user)
            course.save()
            return redirect('course_list')
    
    return render(request, 'course/create.html')


@login_required
def lesson_create(request, course_pk):
   course = get_object_or_404(Course, pk=course_pk)
   if request.method == 'POST':
       title = request.POST.get('title')
       level = request.POST.get('level')
       file = request.FILES.get('file')
      
       if title and level and file:
           lesson = Lesson(course_id=course, title=title, level=level, file=file)
           print('file', file)
           lesson.save()
           return redirect('course_detail', pk=course.pk)
   return render(request, 'course/create_lesson.html', {'course': course})


@login_required
def lesson_detail(request, pk, lesson_pk):
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    return render(request, 'course/lesson_detail.html', {'lesson': lesson})


@login_required
def profile(request):
   return render(request, 'auth/profile.html')


def home(request):
   return render(request, 'home.html')
