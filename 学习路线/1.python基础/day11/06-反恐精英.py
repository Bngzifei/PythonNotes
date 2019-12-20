"""
反恐精英:
一个对象的属性来保存另一个类创建的对象(类似变量保存对象)
a类的方法在b类中的某个方法中a类自行调用.

类图:
class Gun:
属性:
model = # 枪名字

damage = # 杀伤力

bullet = 20

方法:
add_bullet(self,count) # 装子弹
shoot(self,enemy)  # 射击
str:

class Player:
属性:
name = # 角色,警察/匪徒
hp = 100 # 血量
gun = None # 拥有的枪支

方法:

fire(self,enemy) # 开火
hurt(self,enemy_gun)  # 受伤方法,被动调用.
str


多个函数传递数据:1.参数 2.全局变量(直接使用)

面向对象数据传递:1.参数 (临时用一下)2.属性(多个地方使用的时候)来保存一下.


枪和玩家的方法相互调用,玩家要有枪的射击方法,枪要有玩家的受伤

这个写两遍


self.gun.shoot.xx.xxxx.xx = self.cc.vv.bb  #  全部都是=号右边取出来的值赋给左边的第一个属性.

"""


class Gun:
    """枪"""

    def __init__(self, model, damage):
        self.model = model
        self.damage = damage
        self.bullet = 20

    def add_bullet(self, count):
        self.bullet += count

    def shoot(self, enemy):
        """射击"""
        if self.bullet == 0:
            print('无弹,请装弹')
            self.add_bullet(20)  # 自动加20发
        else:
            self.bullet -= 1
            # TODO 敌人会受伤
            enemy.hurt(self)  # 敌人受伤

    def __str__(self):
        return '%s枪:杀伤力:%d,子弹数量:%d' % (self.model, self.damage, self.bullet)


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.gun = None
        self.state = '活的'

    def fire(self, enemy):
        """开火"""
        if self.gun is None:
            print('无枪')
        else:
            self.gun.shoot(enemy)  # 让枪进行射击

    def hurt(self, enemy_gun):
        """受伤"""
        self.hp -= enemy_gun.damage  # 修改自己的血量
        if self.hp > 0:
            print('%s玩家还有%d的血量' % (self.name, self.hp))
        else:
            print('%s玩家挂了' % self.name)
            self.state = '挂了'

    def __str__(self):
        return '%s玩家,当前%s,当前血量%d,持有枪支%s' % (self.name, self.state, self.hp, self.gun)


ak47 = Gun('AK47', 50)
print(ak47)
kar98 = Gun('kar98', 100)
print(kar98)

policeman = Player('警察')
cg = Player('超哥')

policeman.gun = ak47  # 赋值的是对象
cg.gun = kar98
policeman.fire(cg)
cg.fire(policeman)

print(policeman)
print(cg)
