from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAdminUser
from product.models import Product
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from product.api.v1.serializers.product_serializers import ProductSerializer, ProductCreateSerializer
from product.api.v1.services.product_services import ProductServices


class ProductControlView(GenericViewSet, ListModelMixin, CreateModelMixin):
    permission_classes = (IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return ProductCreateSerializer

        return ProductSerializer

    def create(self, request, *args, **kwargs):
        product_serializer = self.get_serializer_class()
        product_serializer = product_serializer(data=request.data, context=dict(user=self.request.user))

        if product_serializer.is_valid(raise_exception=True):
            product_service = ProductServices()

            product = product_service.create_product(product_serializer.validated_data)

            return Response(self.serializer_class(product).data, status=status.HTTP_201_CREATED)
