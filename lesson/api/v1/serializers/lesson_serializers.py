from rest_framework import serializers
from lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'link_to_video', 'product__name']
