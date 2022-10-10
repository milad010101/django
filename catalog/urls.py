from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('book/', views.BookListView.as_view(), name='book'),
    path('namebook/<int:id_book>', views.Toozihat.as_view(), name='namebook'),


]
