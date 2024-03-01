from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from lesson.models import Lesson
from rest_framework.response import Response
from rest_framework import status
from lesson.api.v1.serializers.lesson_serializers import LessonSerializer


class LessonView(GenericViewSet, RetrieveModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            product_id = kwargs['product_id']
            lessons = self.queryset.filter(product_id=product_id, product__userproduct__student=self.request.user)
            return Response(self.serializer_class(lessons, many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)
