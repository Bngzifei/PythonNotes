from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
	page_size = 2  # 默认每页显示2个  最小
	page_size_query_param = 'page_size'  # 默认不写为None  指定前端查询参数的字段
	# page_query_param = 'xx'
	max_page_size = 20  # 每页显示最大数量

# 全局分页
