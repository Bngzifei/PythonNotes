# 定义常量

# 验证码在redis中的过期时间:单位秒
SMS_CODE_REDIS_EXPIRES = 300


# 发送短信间隔时间(秒)  防止用户恶意刷,付费
SEND_FLAG_TIME_INTERVAL = 60