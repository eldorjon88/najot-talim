from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.courses.views import CourseViewSet, CategoryViewSet
from app.teachers.views import TeacherViewSet
from app.students.views import StudentViewSet, EnrollmentViewSet, ContactMessageViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'contact-messages', ContactMessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
