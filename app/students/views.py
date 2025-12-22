from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.students.models import Student, Enrollment, ContactMessage
from .serializers import StudentSerializer, EnrollmentSerializer, ContactMessageSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def enrollments(self, request, pk=None):
        student = self.get_object()
        enrollments = Enrollment.objects.filter(student=student)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    @action(detail=True, methods=['post'])
    def update_progress(self, request, pk=None):
        enrollment = self.get_object()
        progress = request.data.get('progress', 0)
        enrollment.progress = progress
        
        if progress >= 100:
            enrollment.status = 'completed'
            from django.utils import timezone
            enrollment.completed_at = timezone.now()
        
        enrollment.save()
        serializer = self.get_serializer(enrollment)
        return Response(serializer.data)


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    http_method_names = ['get', 'post']
