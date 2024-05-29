from django.contrib import admin
from .models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   list_display = ['title', 'user', 'level', 'subject']
   list_filter = ('level', 'subject', 'user')
   search_fields = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
   list_display = ['title', 'level', 'file', 'course_id']
   list_filter = ('level',)
   search_fields = ('title',)
