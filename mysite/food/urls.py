from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_id>/", views.detail, name="detail"),
    path("item/", views.item, name="item"),
    # add items
    path('add/', views.create_item, name="create-item"),
    # edit
    path("update/<int:id>/", views.update_item, name="update-item"),
    # delete
    path("delete/<int:id>/", views.delete_item, name="delete-item"),
]
