from django.urls import path
from product.api.v1.views.product_views import ProductView
from product.api.v1.views.product_control_views import ProductControlView


urlpatterns = [
    path(
        "list_products/",
        ProductView.as_view({"get": "list"}),
        name="list_products",
    ),
    path(
        "create_product/",
        ProductControlView.as_view({"post": "create"}),
        name="create_product"
    ),
]
