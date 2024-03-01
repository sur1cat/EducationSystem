from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from product.models import Product
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from product.api.v1.serializers.product_serializers import ProductSerializer


class ProductView(GenericViewSet, ListModelMixin, CreateModelMixin):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        try:
            products = self.queryset.filter(start_date__gt=datetime.now())
            return Response(self.serializer_class(products, many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)
