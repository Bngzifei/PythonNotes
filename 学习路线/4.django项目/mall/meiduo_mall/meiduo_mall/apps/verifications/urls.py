from django.conf.urls import url

from . import views

# 注意:要是按照上面from meiduo_mall.meiduo_mall.apps.verifications import views这种写法,
# 就会报如下错误:导包有问题.所以需要 from . import views 这么导包才行
# ImportError: No module named 'meiduo_mall.meiduo_mall'

urlpatterns = [
	# verifications子应用中短信发送的路由
	url(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$',views.SMSCodeView.as_view()),
]