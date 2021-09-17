from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<int:pk>/new_topic/', views.new_topic, name='new_topic'),
    path('board/<int:pk>/', views.board_topics, name='board_topics'),
]
