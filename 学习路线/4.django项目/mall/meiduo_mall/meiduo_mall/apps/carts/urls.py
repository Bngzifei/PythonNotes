from django.conf.urls import url
from . import views

urlpatterns = [
	# 购物车
	url(r'^carts/$', views.CartView.as_view()),
	# 购物车是否全选
	url(r'^carts/selection/$', views.CartSelectAllAPIView.as_view()),
]