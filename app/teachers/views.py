from rest_framework import viewsets
from app.teachers.models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.objects.filter(is_active=True)
    serializer_class = TeacherSerializer
