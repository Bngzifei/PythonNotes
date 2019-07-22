class Gun:
	def __init__(self, model, damage):
		self.model = model  # 枪的型号,就是枪的名字
		self.damage = damage  # 伤害
		self.bullet = 20  # 默认20发

	def add_bullet(self, count):
		self.bullet += count  # 枪装弹

	def shoot(self, enemy):  # 传一个玩家的参数过来,就是Player类
		if self.bullet == 0:
			print('没子弹,装子弹再继续')
			self.bullet += 10  # 自动加子弹
		else:
			self.bullet -= 1
			# TODO 敌人受伤
			enemy.hurt(self)  # 调用玩家的方法

	def __str__(self):
		return '型号:%s,伤害:%d,子弹数量:%d' % (self.model, self.damage, self.bullet)


class Player:
	def __init__(self, role, blood, gun):
		self.role = role  # 角色
		self.blood = blood  # 血量
		self.state = '活着'
		self.gun = gun  # 枪支

	# self.gun = None  # 枪支

	# TODO 攻击敌人

	def kill(self, enemy):  # enemy 实际传递的是一个对象 (玩家Player的对象)
		if self.gun is None:
			print('没有枪,请拿枪')
		else:
			self.gun.shoot(enemy)  # 调用枪的shoot方法

	def hurt(self, enemy_gun):  # enemy_gun 实际传的是一个枪的对象,所以后面就可以调用枪的一切属性    对象.方法 的方式来调用
		self.blood -= enemy_gun.damage  # 参数只需要传一个枪,通过 枪.伤害  来调用枪的属性-->枪的伤害值.   敌人枪支的伤害

		if self.blood < 0:
			self.state = '已死亡'
			print('玩家:%s,状态:%s,当前血量为%d' % (self.role, self.state, self.blood))
		else:
			self.state = '已受伤'
			print('玩家:%s,状态:%s,当前血量为%d' % (self.role, self.state, self.blood))

	def __str__(self):
		return '玩家:%s,状态:%s,血量:%d,枪的型号:%s' % (self.role, self.state, self.blood, self.gun)


ak47 = Gun('ak47', 500)
ak48 = Gun('ak48', 20)
print(ak47)
print(ak48)

pman = Player('警察', 100, ak48)
feitu = Player('匪徒', 100, ak47)

pman.kill(feitu)
feitu.kill(pman)

print(pman)
print(feitu)
