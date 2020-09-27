from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('NoResult', views.NoResult),
	path('box',views.index_boxed),
	path('classic',views.index_classic),
	path('fashion',views.index_fashion),
	path('landing',views.index_landing),
]