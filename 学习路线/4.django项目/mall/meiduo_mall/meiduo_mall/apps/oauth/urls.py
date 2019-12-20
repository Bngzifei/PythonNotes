from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^qq/authorization/$',views.QQAuthURLView.as_view()),  # 1.返回扫码界面的url
	url(r'^qq/user/$',views.QQAuthUserView.as_view()),  # 2.qq OAuth2.0 认证
]