from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Course(models.Model):
    user = models.ForeignKey(
        User, 
        related_name='courses',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255, blank=False)
    level = models.PositiveIntegerField()
    subject = models.CharField(max_length=255, blank=False)

    class Meta:
        ordering = ['title']


class Lesson(models.Model):
    title = models.CharField(max_length=255, blank=False)
    level = models.PositiveIntegerField()
    course_id = models.ForeignKey(
        'Course',
        related_name='lessons',
        on_delete=models.CASCADE,
    )
    file = models.FileField(upload_to='lessons/')

    class Meta:
        ordering = ['title']
