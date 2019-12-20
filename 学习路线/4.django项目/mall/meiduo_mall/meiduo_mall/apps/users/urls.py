from django.conf.urls import url
from rest_framework import routers

from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
	# 注册路由
	url(r'^users/$', views.UserView.as_view()),
	# 判断用户名是否存在
	url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),
	# 判断手机号是否存在
	url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),

	# JWT登录
    # url(r'^authorizations/$', ObtainJSONWebToken.as_view())
    # url(r'^authorizations/$', obtain_jwt_token),
	# 在此处要进行购物车的cookie合并到redis
	url(r'^authorizations/$', views.UserAuthorizeView.as_view()),

	# 用户详情
	url(r'^user/$', views.UserDetailView.as_view()),

	# 设置邮箱
	url(r'^email/$', views.EmailView.as_view()),

	# 校验邮箱链接
	url(r'^emails/verification/$', views.VerifyEmailView.as_view()),

	# 用户浏览记录
	url(r'^browse_histories/$', views.UserBroweHistoryView.as_view()),

]

# 视图集:就得使用路由器
router = routers.DefaultRouter()
router.register(r'addresses', views.AddressViewSet, base_name='addresses')

urlpatterns += router.urls


# POST /addresses/ 新建  -> create
# PUT /addresses/<pk>/ 修改  -> update
# GET /addresses/  查询  -> list
# DELETE /addresses/<pk>/  删除 -> destroy
# PUT /addresses/<pk>/status/ 设置默认 -> status
# PUT /addresses/<pk>/title/  设置标题 -> title




"""
注意:校验只能在这台虚拟机里面进行网页校验,在windows跨机器里不能进行校验


"""