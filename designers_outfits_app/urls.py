from django.urls import path
from . import views

urlpatterns = [
	path('not_found', views.not_found),
	path('blog',views.blog_landing),
	path('fashion',views.index_fashion),
	path('landing',views.index_landing),
	path('product/<int:id>',views.product),
]