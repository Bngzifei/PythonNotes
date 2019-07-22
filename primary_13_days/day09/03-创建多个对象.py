class Dog:
	def drink(self):
		print('喝娃哈哈')

	def eat(self):
		print('吃排骨')


# 类中定义的方法会被此类创建出来的所有对象共享
dog1 = Dog()  # <__main__.Dog object at 0x000002481333B8D0> 写一次就是一个新的对象.内存地址值肯定不一样
dog2 = Dog()  # <__main__.Dog object at 0x000002481333BAC8>写一次就是一个新的对象.内存地址值肯定不一样
print(dog1)
print(dog2)

dog1.drink()
dog2.drink()

# 方法是共有的,但是属性是每一个对象所独有的,各自记录各自的数据
dog1.name = 'xiaohei'
dog2.name = 'xiaohua'
# 两个同类型的对象,可以有同名的属性,互不影响.同名的属性是各自记录各自的数据.私有的
print(dog1.name)
print(dog2.name)

dog1.age = 2

# 类:前后空2行  类在第一行时不用这么写
