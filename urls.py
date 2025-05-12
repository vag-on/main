from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.NewsList.as_view(), name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('review/add/', views.ReviewCreate.as_view(), name='review_create'),
    path('emergency-commissioner/', views.emergency_commissioner, name='emergency_commissioner'),
    path('independent-expertise/', views.independent_expertise, name='independent_expertise'),
    path('auto-lawyer/', views.auto_lawyer, name='auto_lawyer'),
]
