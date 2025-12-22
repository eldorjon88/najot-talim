from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from app.courses.models import Course, Category, Lesson
from .serializers import CourseSerializer, CourseDetailSerializer, CategorySerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'difficulty']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'price', 'rating', 'students_count']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    @action(detail=False, methods=['get'])
    def popular(self, request):
        popular_courses = Course.objects.filter(is_active=True).order_by('-students_count')[:6]
        serializer = self.get_serializer(popular_courses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_id = request.query_params.get('category_id')
        if category_id:
            courses = Course.objects.filter(category_id=category_id, is_active=True)
            serializer = self.get_serializer(courses, many=True)
            return Response(serializer.data)
        return Response({'error': 'category_id is required'}, status=400)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
