from django.urls import path
from .views import PageListView, PageDetailView
urlpatterns = [
    # path('', views.pages, name='pages'),
    path('', PageListView.as_view(), name='pages'),
    # path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
]
