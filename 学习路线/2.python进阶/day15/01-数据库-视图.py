print('-------------')
"""
视图:
select goods.name,goods_cates.name,goods_brands.name from goods,goods_cates,goods_brands where goods.cate_id=goods_cates.id and goods_brands.id=goods.brand_id

太tm的长了.

视图就把这些复杂操作封装起来了,底层给我们进行三张表的合并查询操作.

1.>创建视图:  create view 视图名称 as select 语句<多张表的操作>;

意义:封装了对多张表的复杂操作.

示例:
create view v_goods_info as
 select goods.name gname,goods_cates.name cname,goods_brands.name bname
 from goods,goods_cates,goods_brands 
 where goods.cate_id=goods_cates.id 
 and goods_brands.id=goods.brand_id;

技巧:sql语句很长的时候记得以关键字断句.

注意:字段名不可以重复,有重名的情况下必须起别名

查看:show tables;
所以建议视图以v开头 区别基本表和视图
使用:select 字段 from 视图 where ...;
连接查询也可以,和基本表的操作完全一致

视图只是一个表结构,没有保存任何基本表的表数据.只是一个虚表,不占数据库内存.
在用户需要查询视图的时候,再去基本表中取出对应的数据
只给用户展示指定字段,屏蔽了其他字段,从而显得更安全.

2.>删除视图:
drop view 视图名;
不建议通过视图表去修改基本表的数据
需要修改基本表,直接对基本表进行修改操作即可

"""
# ------------------------------------创建视图:------------------------------->
"""
# create view v_goods_info as select goods.name gname,goods_cates.name cname,goods_brands.name bname 
from goods,goods_cates,goods_brands where goods.cate_id=goods_cates.id and goods_brands.id=goods.brand_id;
show tables;
+--------------+
| Tables_in_jd |
+--------------+
| gongfu       |
| goods        |
| goods_brands |
| goods_cates  |
| hero         |
| v_goods_info |
+--------------+
"""

"""查询视图:

select * from v_goods_info;
+---------------------------------+---------------+-------+
| gname                           | cname         | bname |
+---------------------------------+---------------+-------+
| r510vc 15.6英寸笔记本           | 笔记本        | 华硕  |
| y400n 14.0英寸笔记本电脑        | 笔记本        | 联想  |
| g150th 15.6英寸游戏本           | 游戏本        | 雷神  |
| x550cc 15.6英寸笔记本           | 笔记本        | 华硕  |
| x240 超极本                     | 超级本        | 联想  |
| u330p 13.3英寸超极本            | 超级本        | 联想  |
| svp13226scb 触控超极本          | 超级本        | 索尼  |
| ipad mini 7.9英寸平板电脑       | 平板电脑      | 苹果  |
| ipad air 9.7英寸平板电脑        | 平板电脑      | 苹果  |
| ipad mini 配备 retina 显示屏    | 平板电脑      | 苹果  |
| ideacentre c340 20英寸一体电脑  | 台式机        | 联想  |
| vostro 3800-r1206 台式电脑      | 台式机        | 戴尔  |
| imac me086ch/a 21.5英寸一体电脑 | 台式机        | 苹果  |
| at7-7414lp 台式电脑 linux ）    | 台式机        | 宏碁  |
| z220sff f4f06pa工作站           | 服务器/工作站 | 惠普  |
| poweredge ii服务器              | 服务器/工作站 | 戴尔  |
| mac pro专业级台式电脑           | 服务器/工作站 | 苹果  |
| hmz-t3w 头戴显示设备            | 笔记本配件    | 索尼  |
| 商务双肩背包                    | 笔记本配件    | 索尼  |
| x3250 m4机架式服务器            | 服务器/工作站 | ibm   |
| 商务双肩背包                    | 笔记本配件    | 索尼  |
+---------------------------------+---------------+-------+

"""
"""
验证视图是否保存数据:不保存数据,只是在使用的时候直接去基本表获取数据.
在基本表 表中修改了数据之后,在视图中可以查看到,说明视图是依赖于基本表的.
也说明只有在使用视图的时候视图会去调用基本表的数据
# update goods set name='LV包' where id =1;
Query OK, 1 row affected
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from v_goods_info;
+---------------------------------+---------------+-------+
| gname                           | cname         | bname |
+---------------------------------+---------------+-------+
| LV包                            | 笔记本        | 华硕  |
| y400n 14.0英寸笔记本电脑        | 笔记本        | 联想  |
| g150th 15.6英寸游戏本           | 游戏本        | 雷神  |
| x550cc 15.6英寸笔记本           | 笔记本        | 华硕  |
| x240 超极本                     | 超级本        | 联想  |
| u330p 13.3英寸超极本            | 超级本        | 联想  |
| svp13226scb 触控超极本          | 超级本        | 索尼  |
| ipad mini 7.9英寸平板电脑       | 平板电脑      | 苹果  |
| ipad air 9.7英寸平板电脑        | 平板电脑      | 苹果  |
| ipad mini 配备 retina 显示屏    | 平板电脑      | 苹果  |
| ideacentre c340 20英寸一体电脑  | 台式机        | 联想  |
| vostro 3800-r1206 台式电脑      | 台式机        | 戴尔  |
| imac me086ch/a 21.5英寸一体电脑 | 台式机        | 苹果  |
| at7-7414lp 台式电脑 linux ）    | 台式机        | 宏碁  |
| z220sff f4f06pa工作站           | 服务器/工作站 | 惠普  |
| poweredge ii服务器              | 服务器/工作站 | 戴尔  |
| mac pro专业级台式电脑           | 服务器/工作站 | 苹果  |
| hmz-t3w 头戴显示设备            | 笔记本配件    | 索尼  |
| 商务双肩背包                    | 笔记本配件    | 索尼  |
| x3250 m4机架式服务器            | 服务器/工作站 | ibm   |
| 商务双肩背包                    | 笔记本配件    | 索尼  |
+---------------------------------+---------------+-------+

"""