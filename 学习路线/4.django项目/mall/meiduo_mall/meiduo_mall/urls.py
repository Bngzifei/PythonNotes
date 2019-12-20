"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),   # 富⽂文本编辑器器

    # 后面都是自己的,前面都是系统自有的
    url(r'^',include('verifications.urls')),  # 短信发送的路由
    url(r'^',include('users.urls')),  # 用户的路由
    url(r'^oauth/',include('oauth.urls')),  # qq第三方登录
    url(r'^',include('areas.urls')),  # 省市区
    url(r'^',include('goods.urls')),  # 商品模块
    url(r'^',include('carts.urls')),  # 购物车模块

]
