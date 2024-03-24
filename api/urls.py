from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'teachers', views.TeacherViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'classes', views.ClassViewSet)
router.register(r'journals', views.JournalViewSet)
router.register(r'subjects', views.SubjectViewSet)


urlpatterns = [
    path('', include(router.urls)),
]