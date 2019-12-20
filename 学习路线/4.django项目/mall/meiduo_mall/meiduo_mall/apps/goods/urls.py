from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
	url(r'^categories/(?P<pk>\d+)/$', views.CategoryView.as_view()),
	url(r'^categories/(?P<category_id>\d+)/skus/$', views.SKUListView.as_view()),
]

# 使用了视图集,所以需要使用路由器
router = DefaultRouter()
router.register('skus/search', views.SKUSearchViewSet, base_name='skus_search')

urlpatterns += router.urls

# 默认:创建的时间倒序排
