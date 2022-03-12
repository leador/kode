from django.urls import path

from . import views

urlpatterns = [
    path('', views.news_list, name='home'),
    path('category/<category_slug>/', views.news_by_category, name='category'),
    path('<news_slug>/', views.ViewNews.as_view(), name='view_news'),
]
