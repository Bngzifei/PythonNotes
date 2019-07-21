import time

def gettime():
	"""当用户请求/gettime.html的时候 执行当前函数"""
	return time.ctime()

def app(data_dict):
	if data_dict['PATH_INFO'] == '/gettime.html':
		return '200 OK',[('Content-Type','text/html')],'hello this is response body'