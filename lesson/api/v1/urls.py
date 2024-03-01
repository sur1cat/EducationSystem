from django.urls import path
from lesson.api.v1.views.lessons_view import LessonView


urlpatterns = [
    path(
        "list_user_lessons/<int:product_id>/",
        LessonView.as_view({"get": "retrieve"}),
        name="list_products",
    ),
]
