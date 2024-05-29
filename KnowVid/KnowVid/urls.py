from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings, urls
from django.views.generic import TemplateView
from KnowVid.apps.courses import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('home/', views.home, name='home'),
   path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
   path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('admin/', admin.site.urls),
   path('courses/', views.course_list, name='course_list'),
   path('courses/<int:pk>/', views.course_detail, name='course_detail'),
   path('courses/create/', views.course_create, name='course_create'),
   path('courses/<int:course_pk>/create_lesson/', views.lesson_create, name='lesson_create'),
   path('accounts/profile/', views.profile, name='profile'),
   path('logged_out/', TemplateView.as_view(template_name='registration/logged_out.html'), name='logged_out'),
   path('courses/<int:pk>/lessons/<int:lesson_pk>', views.lesson_detail, name='lesson_detail'),  # Новий маршрут
]


if settings.DEBUG:
    urlpatterns +=[
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        })
    ]