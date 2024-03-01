from decimal import Decimal

from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'lesson_count']

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=155, required=True)
    start_date = serializers.DateTimeField(required=True)
    price = serializers.DecimalField(required=True)

    def validate(self, attrs):
        user = self.context['user']
        price = attrs['price']

        if not user.is_superuser or not user.is_author:
            raise Exception({"permission error": "user neither author or admin"})

        if not price > Decimal("0"):
            raise Exception({"amount error"})

        attrs['author'] = user

        return attrs
