# coding:utf-8
import requests

RHEL7_URL = "https://access.redhat.com/downloads/content/rhel---7.4/x86_64/4118/kernel/3.10.0-693.39.1.el7/src/fd431d51/package-changelog"
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
ACCOUNT = "rd.sangfor@gmail.com"
PASSWORD = "@Sangfor123"
LOGIN_URL = "https://access.redhat.com/login"

session_obj = requests.Session()

LOGIN_POST_URL = "https://access.redhat.com/auth/realms/redhat-external/login-actions/authenticate"

response = session_obj.post(LOGIN_POST_URL)
if response.status_code == 200:
	print(response.text)
