"""
要求:

1.游戏枪支有不同的型号，并拥有不同的伤害
2.枪支可以添加一定数量的子弹
3.枪支可以射击敌人，射击敌人时，如果子弹数量为0，则提示玩家；如果有子弹，会减少子弹，如果击中敌人，会让敌人受伤
4.输出枪支信息时，可以显示枪支的型号、伤害、子弹数量 ————————————————————————————————————————————————
5.游戏玩家分为警察和匪徒两种角色，玩家拥有自己的枪支和血量，可以攻击敌人
6.玩家攻击敌人时，如果没有枪，则提示玩家；如果有枪，则检查枪支是否有子弹，有子弹则使用枪支射击敌人，没有子弹则自动给枪支添加子弹
7.玩家被击中会受伤，减血量为枪支的伤害，提示玩家受伤并显示当前血量；如果血量<=0，则提示玩家死亡
8.输出玩家信息时，可以显示玩家角色、状态、血量、所持枪的信息

类图:  就是找属性和方法
class Gun:
属性:
type = # 枪的名字
damage = # 枪的威力,伤害
bullet = # 枪的子弹数量

方法:

add_bullet()# 装子弹
shoot() # 射击敌人

str() # 方法返回信息



class Role:  # 玩家角色类
属性:
role_type: # 角色类型
blood_num: # 血量
own_gun: # 持有的枪  注意:这就要求传入Gun类产生的实例对象 gun
方法:
kill(enemy,gun)  # 杀死敌人,注意:这里是需要传入一个Role类产生的实例化对象role.需要拿自己拥有的gun去kill敌人.这个方法实现的操作就是使用gun的shoot方法去杀enemy.

hurted()  # 减血量是枪的伤害,说明有一个blood_num - damage 的操作在这个方法里面.


"""


class Gun:
    def __init__(self, type, damage, bullet):
        self.type = type  # 枪的名字,字符串
        self.damage = damage  # 枪的伤害值,整型
        self.bullet = bullet  # 子弹数目,整型

    def add_bullet(self, count):
        self.bullet += count  # 加指定数目的子弹整型

    def shoot(self, enemy):  # 射击敌人,需要有一个参数来记录 敌人
        if self.bullet is None:
            print('没子弹了,请先加子弹')
            self.add_bullet(15)
        else:
            self.bullet -= 1  # 减少子弹
            enemy.hurted(self)  # 意思就是这把枪让敌人受伤了.枪导致 敌人的受伤方法调用,执行了.

    def __str__(self):
        return '枪名:%s,枪的威力:%d,子弹数量:%d' % (self.type, self.damage, self.bullet)


class Role:
    def __init__(self, role_type, blood_num, owe_gun):
        self.role_type = role_type
        self.blood_num = blood_num
        self.own_gun = owe_gun
        self.status = '活的好好的'

    def kill(self, enemy):
        self.own_gun.shoot(enemy)

    def hurted(self, enemy_gun):
        self.blood_num -= enemy_gun.damage  # 减血量是敌人的枪的伤害值,这里需要先进行减掉血量的操作,如果放到else判断里面,那么会跳过第一次的减血进行判断,会出现判断错误的情况
        if self.blood_num <= 0:
            self.status = '死了'
            print('角色:%s目前的状态是:%s' % (self.role_type, self.status))
        else:
            self.status = '受伤了'
            print('角色:%s目前的状态是:%s,当前血量是:%d' % (self.role_type, self.status, self.blood_num))

    def __str__(self):
        return '角色:%s目前的状态是:%s,当前血量是:%d,持有的枪型是:%s' % (self.role_type, self.status, self.blood_num, self.own_gun)


# 先创建两把枪
ak = Gun('ak47', 20, 50)
wusi = Gun('54', 10, 40)

# 创建两个玩家角色
police = Role('警察', 100, wusi)
feitu = Role('匪徒', 90, ak)

# 警察杀匪徒,匪徒杀警察
police.kill(feitu)
feitu.kill(police)

police.kill(feitu)
feitu.kill(police)

police.kill(feitu)
feitu.kill(police)

police.kill(feitu)
feitu.kill(police)

police.kill(feitu)
feitu.kill(police)

# police.kill(feitu)
# feitu.kill(police)
# 输出警察和匪徒的当前状态
print(police)
print(feitu)
