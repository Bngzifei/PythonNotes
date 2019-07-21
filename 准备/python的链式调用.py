class Test:
	def __init__(self):
		self.res = None

	def talk(self):
		print('talking')
		self.res = 1
		return self

	def run(self):
		print('running')
		self.res += 10
		return self


t = Test()
ret = t.talk().run().res  # python的链式调用
print(ret)

"""
输出:
talking
running
11

"""
