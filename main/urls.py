from django.urls import path, include
from . import views

urlpatterns = [
  
    path('', views.index, name='index'),
    path('stk-push-callback/', views.stk_push_callback, name='stk_push_callback'),
]