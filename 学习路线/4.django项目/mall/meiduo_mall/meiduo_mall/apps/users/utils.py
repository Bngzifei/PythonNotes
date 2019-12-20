
from django.contrib.auth.backends import ModelBackend
import re
from .models import User

def get_user_by_account(account):
    """
    根据account 动态查找用户user
    :param account: 此参数有可能是用户名,也有可能是手机号
    :return: user
    """
    try:
        if re.match('^1[3-9]\d{9}$', account):
            user = User.objects.get(mobile=account)
        else:
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user





class UsernameMobileAuthBackend(ModelBackend):
    """修改后端登录的认证系统,使用多账号登录"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        :param request: 本次提供认证的请求体
        :param username: 本次认证的账号, 账号可以是'用户名或手机号'
        :param password: 本次认证用户的密码
        :return: 如果认证成功返回user对象或否则抛出异常
        """

        # 1.根据账户去查询user
        # user = 动态查询用户'用户名或手机号'
        user = get_user_by_account(username)
        # 2.判断用户是否存在,并且验证密码是否正确
        if user and user.check_password(password):
            return user
# 重写jwt登录成功后的返回数据函数,多加上自己要返回的id和username
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }
