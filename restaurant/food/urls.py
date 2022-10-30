from . import views
from django.urls import path

app_name = "food"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("<int:pk>/", views.Detail.as_view(), name="detail"),
    path("add", views.CreateItem.as_view(), name="create_item"),
    path("update/<int:id>", views.update_item, name="update_item"),
    path("delete/<int:id>", views.delete_item, name="delete_item"),
]
