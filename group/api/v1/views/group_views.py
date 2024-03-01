from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from group.models import Group
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from group.api.v1.services.group_services import GroupService


class GroupView(GenericViewSet, CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            product = Product.objects.filter(userproduct__student=self.request.user).last()

            group_service = GroupService()
            try:
                group_service.distribute_users_to_groups(product=product, user=self.request.user)

                return Response({"success"}, status=status.HTTP_200_OK)

            except Exception as e:
                raise e

        except Exception as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)
