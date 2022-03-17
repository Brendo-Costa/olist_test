from django.urls import path
from . import views

urlpatterns = [
    path('', views.Create_Book.as_view(), name='create_book'),
    #path('', views.List_Book.as_view(), name='create_book'),
    #path('update/<pk>', views.Update_Book.as_view(), name='create_book'),
    #path('delete/<pk>', views.Delete_Book.as_view(), name='create_book'),
]