print('--------------------------------------------')
"""
1.> as 起别名
	1.>给字段起别名:select id as '学号',name as '芳名'from students;
	2.>给表起别名:select s.id,s.name from students as s;
注意:as可以不写,省略.
select s.id,s.name from students s;

2.>去重:distinct
	select distinct gender from students;
	多个字段:
	select distinct age,gender from students;
	满足age和gender都一样的记录才会被去除,只有age或者gender一样的不会被去掉.
	
3.> where 筛选:
从表<集合>筛选出满足条件的记录<记录就是行数据>
	select * from students where age=18;
	select * from students where age>18;
	select * from students where age<18;
	select * from students where age>=18;
	select * from students where age<=18;
	# != 等价于 <>
	select * from students where age!=18;
	select * from students where age<>18;
	
	18到30岁的
	select * from students where age between 18 and 30;
	select * from students where age>18 and age<30;
	或者:or
	select * from students where age>18 or gender=1;
	取反 not: age不大于18的
	select * from students where not age>18;
	
	# 这种是错误的,mysql中没有这种形式
	select * from students where 18<age<30;
	
4.>enum():枚举本质是数字,从1开始
enum('男','女','中性','保密') 对应关系是 1-->男,2-->女,3-->中性,4-->保密

utf8中%这种可以匹配多个字节

5.>like模糊查询:
	% --> 匹配任意个任意字符  类似于正则的*
	_ --> 匹配一个任意字符    类似于正则的?
	
	# 表示name中以王开头的,王x或者王xxxxxxx,均可
	select * from students where name like '王%';
	
	# 表示name中以王开头的,只能是王x这种格式的
	select * from students where name like '王_';
	
	#一般常用:表示查询表中指定字段name中含有指定字符王的记录
	select * from students where name like '%王%';
	
	# 不含有王的
	select * from students where name not like '%王%';

6.>范围查询:
	age=18或者age=28或者age=38
	select * from where age in (18,28,38);
	
	age!=18或者age!=28或者age!=38
	select * from where age not in (18,28,38);
	
	between...and...:表示连续范围
	select * from where age between 18 and 45;闭区间,可以取到上下限
	
	# 不在这个范围内
	select * from where age not between 18 and 45;

7.>判断是否为空: is null
	NULL是一种状态,不是具体的数据,所以不可以使用=NULL去判断
	只能使用is NULL表示,意为是否为空
	
	# 是空  不区分大小写 所以null和NULL均可以.
	select * from students where height is null;
	
	# 是非空 is not NULL   而不是not is NULL
	select * from students where height is not NULL;
	
8.>排序: order by 字段名; 默认是升序 asc-->ascend:上升  
		降序使用desc<PS注意和描述表结构里面的desc 表名 区分> ---> descend:下降
		asc:默认升序,可以不写
	select * from students order by age desc;
	
	# 组合使用:建议多个条件时候的and往前写
	select * from students where gender=1 and age between 18 and 58 order by age;
	
	# order by后面可以跟上多个字段. 先按身高height降序排,相同身高的按年龄age升序排
	select * from students where gender=2 and age between 18 and 58 order by height desc,age asc;

9.> 分页:搜索结果部分显示  按照用户的条件

limit 0,9  --->   0表示数据的起始下标,9表示一页显示的数据的数量

limit 数量 * (页面-1),数量
一般和排序合在一起使用:就是将结果部分显示
select * from students order by height desc limit 3;
select * from students order by height desc limit 0,3;
# 把最高的去掉之后的最高
select * from students order by height desc limit 1,3;

limit分页的数据是可以不排序的,需要排序得加order by
如果是日常生活说第一个,那就是1开始的,但是数据检索的时候第一条数据是0开始计数的.注意区分.
# 身高第四到第八:
select * from students order by height desc limit 3,5;
#限制查询出来的数据是2条
select * from students where gender=1 limit 2;
# 查询前5个数据
select * from students limit 5
# 每页显示2个,第一个页面是0,1
select * from students limit 0,2;
第2个页面是0,1
select * from students limit 2,2;
3个页面是2,3
select * from students limit 4,2;
4个页面是4,5
select * from students limit 6,2;
#主要是电商网站分页显示
n个页面:每个页面显示m条数据
select * from students limit m*(n-1),m;
# 每页2条,显示第6页的,
select * from students order by age limit 10,2;

"""
# --------------------------------聚合函数------------------------->
"""
sum/min/count/max/avg  就是把多个数据合成一个数据
组函数:对一组数据进行统计
特点:忽略字段为NULL的记录
不允许出现嵌套 count(sum(height)) 因为sum()返回的是一个数据,不是一组数据,所以绝对不能嵌套.

1.>count(*):统计,有多少,总数 *表示任意,
select count(height) from students; height字段中不为空的
select count(*) from students; 所有的,包括空的
对性别统计总数
select count(distinct gender) from students;

2.>max():最大
select max(height),max(age) from students;

3.>min():最小
select min(height) from students where gender=1;

4.sum():求和
select sum(height)/count(height) from students where gender=2;
select avg(height) from students where gender=2;


5.>round():四舍五入
round(参数1,参数2)不是组函数,参数1是一个数字,参数2是一个整数,表示保留的小数位数.

	select round(122.34567890,5);
	+-----------------------+
	| round(122.34567890,5) |
	+-----------------------+
	|             122.34568 |
	+-----------------------+


select round(avg(age)) from students;  输出28,不写就是整数
select round(avg(age),2) from students; 输出 27.64  保留2位小数

# 男性平均年龄
select round(avg(age),2) as '男性平均年龄' from students where gender=1;
输出:
+--------------------+
| 男性平均年龄       |
+--------------------+
|              32.60 |
+--------------------+
ps:浮点数<即小数>在数据库中不是精确存储的,不要进行精确匹配=,只能进行大于小于等

"""
# ---------------------------------分组:group by ----------------------->
"""
聚合函数:
默认情况下没有分组的情况 是对整个表进行统计计算
但是,如果分组了,就是对分组后的每个组进行统计计算.
"""

"""
1.>group by:
SQL语句只能对二维的数据表进行操作.
select * from students group by gender;这样是错误的

select gender from students group by gender;只能查看我们进行分组group by 后面的字段
+--------+
| gender |
+--------+
| 男     |
| 女     |
| 中性   |
| 保密   |
+--------+

计算每种性别及对应的人数
select count(*)from students group by gender;
+----------+
| count(*) |
+----------+
|        5 |
|        7 |
|        1 |
|        1 |
+----------+
注意:一旦分组和聚合函数合用,聚合函数不再统计整体结果,而是统计每个小组的结果

查找性别及对应的每个性别的平均年龄:
select gender,avg(age)from students group by gender;
+--------+----------+
| gender | avg(age) |
+--------+----------+
| 男     |  32.6000 |
| 女     |  23.2857 |
| 中性   |  33.0000 |
| 保密   |  28.0000 |
+--------+----------+

扩展:select 后面的字段,要么是group by分组后面的字段,要么是放在聚合函数中的,其余情况都会出错 

显示具体的分组中每个成员的某个字段的数据,并且拼接显示在一起--->group_concat()
select gender,avg(age),group_concat(age) from students group by gender;
+--------+----------+----------------------+
| gender | avg(age) | group_concat(age)    |
+--------+----------+----------------------+
| 男     |  32.6000 | 29,59,36,27,12       |
| 女     |  23.2857 | 18,18,38,18,25,12,34 |
| 中性   |  33.0000 | 33                   |
| 保密   |  28.0000 | 28                   |
+--------+----------+----------------------+

注意: 起别名的as 可以不写,直接在字段名后面跟 新名字,不要加,号
select group_concat(name) '姓名',group_concat(age) '年龄',gender,avg(age) '平均年龄
' from students group by gender;
+------------------------------------------+----------------------+--------+----------+
| 姓名                                     | 年龄                 | gender | 平均年龄 |
+------------------------------------------+----------------------+--------+----------+
| 彭于晏,刘德华,周杰伦,程坤,郭靖           | 29,59,36,27,12       | 男     | 32.6     |
| 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰 | 18,18,38,18,25,12,34 | 女     | 23.2857  |
| 金星                                     | 33                   | 中性   | 33       |
| 凤姐                                     | 28                   | 保密   | 28       |
+------------------------------------------+----------------------+--------+----------+

select gender,name from students group by gender; --->这样是错误的
select gender,group_concat(name) from students group by gender;
+--------+-----------------------------------------------------------+
| gender | group_concat(name)                                        |
+--------+-----------------------------------------------------------+
| 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                            |
| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                  |
| 中性   | 金星                                                      |
| 保密   | 凤姐                                                      |
+--------+-----------------------------------------------------------+

select gender,group_concat(name),count(*) from students group by gender;
+--------+-----------------------------------------------------------+----------+
| gender | group_concat(name)                                        | count(*) |
+--------+-----------------------------------------------------------+----------+
| 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                            |        5 |
| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                  |        7 |
| 中性   | 金星                                                      |        1 |
| 保密   | 凤姐                                                      |        1 |
+--------+-----------------------------------------------------------+----------+

2.>having: 对分组加条件进行筛选.和where不同,where是对表数据筛选
select gender,group_concat(name),count(*) from students group by gender having count(*)>2;
+--------+-----------------------------------------------------------+----------+
| gender | group_concat(name)                                        | count(*) |
+--------+-----------------------------------------------------------+----------+
| 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                            |        5 |
| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                  |        7 |
+--------+-----------------------------------------------------------+----------+
select gender,group_concat(name) from students group by gender having avg(age) <= 30;

select gender,group_concat(name) from students group by gender having avg(age) <= 30;
+--------+-----------------------------------------------------------+
| gender | group_concat(name)                                        |
+--------+-----------------------------------------------------------+
| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                  |
| 保密   | 凤姐                                                      |
+--------+-----------------------------------------------------------+

select gender,group_concat(name) from students group by gender having count(*) <= 5;
+--------+-----------------------------------------------------------+
| gender | group_concat(name)                                        |
+--------+-----------------------------------------------------------+
| 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                            |
| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                  |
| 中性   | 金星                                                      |
| 保密   | 凤姐                                                      |
+--------+-----------------------------------------------------------+

汇总显示:with rollup
select gender,group_concat(name) from students group by gender with rollup; +--------+---------------------------------------------------------------------------------------------------------------------+
| gender | group_concat(name)                                                                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------+
| 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                                                                      |
| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                                                                            |
| 中性   | 金星                                                                                                                |
| 保密   | 凤姐                                                                                                                |
| NULL   | 彭于晏,刘德华,周杰伦,程坤,郭靖,小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰,金星,凤姐                                   |
+--------+---------------------------------------------------------------------------------------------------------------------+

"""
# -------------------------------连接-------------------------------->
"""
应用场景:当需要把多张表的数据汇总在一张表里面显示的时候,需要使用连接.
A:A是左表   B:B是右表
1.>内连接:A B两个表有关联的地方显示在一张表中显示

外连接是建立在内连接的基础上.
2.>右连接:<外连接> 内连接+ 额外数据如果来自右表,称之为右连接
3.>左连接:<外连接> 内连接+ 额外数据如果来自左表,称之为左连接

内连接:求两个表关联的数据
外连接:在内连接的基础上 添加外部数据,来自左边,左外来自右边,右外.

笛卡尔积:左表和右表中的每一条记录分别进行拼接组合.
关联:不一定是相等,可以大于,小于,或者大于等于等等
select * from hero join gongfu;
就把hero join gongfu当做一张表就好.是hero和gongfu两张表合并之后的新表
join或者cross join  
需要的数据就在笛卡尔积里面出现了.如何把这些需要的数据筛选出来才是王道

+----+-----------+----------+----+--------------+
| id | name      | kongfuid | id | kongfu       |
+----+-----------+----------+----+--------------+
|  1 | 妲己      |        2 |  1 | 吟诗作对     |
|  2 | 李白      |        1 |  1 | 吟诗作对     |
|  3 | 程咬金    |        3 |  1 | 吟诗作对     |
|  4 | 共孙俪    |        5 |  1 | 吟诗作对     |
|  1 | 妲己      |        2 |  2 | 推心置腹     |
|  2 | 李白      |        1 |  2 | 推心置腹     |
|  3 | 程咬金    |        3 |  2 | 推心置腹     |
|  4 | 共孙俪    |        5 |  2 | 推心置腹     |
|  1 | 妲己      |        2 |  3 | 半路杀出     |
|  2 | 李白      |        1 |  3 | 半路杀出     |
|  3 | 程咬金    |        3 |  3 | 半路杀出     |
|  4 | 共孙俪    |        5 |  3 | 半路杀出     |
|  1 | 妲己      |        2 |  4 | 沉默是金     |
|  2 | 李白      |        1 |  4 | 沉默是金     |
|  3 | 程咬金    |        3 |  4 | 沉默是金     |
|  4 | 共孙俪    |        5 |  4 | 沉默是金     |
+----+-----------+----------+----+--------------+

表和表之间关联的字段,这里是kongfuid和kongfu表中id一致

on:后面加上条件判断   
inner 可以省略

select * from hero inner join gongfu on hero.kongfuid=gongfu.id;
select * from hero join gongfu on hero.kongfuid=gongfu.id;
+----+-----------+----------+----+--------------+
| id | name      | kongfuid | id | kongfu       |
+----+-----------+----------+----+--------------+
|  2 | 李白      |        1 |  1 | 吟诗作对     |
|  1 | 妲己      |        2 |  2 | 推心置腹     |
|  3 | 程咬金    |        3 |  3 | 半路杀出     |
+----+-----------+----------+----+--------------+

左外连接:outer 可以省略不写,多个左表的数据
select * from hero left outer join gongfu on hero.kongfuid=gongfu.id;
select * from hero left join gongfu on hero.kongfuid=gongfu.id;
+----+-----------+----------+------+--------------+
| id | name      | kongfuid | id   | kongfu       |
+----+-----------+----------+------+--------------+
|  2 | 李白      |        1 |    1 | 吟诗作对     |
|  1 | 妲己      |        2 |    2 | 推心置腹     |
|  3 | 程咬金    |        3 |    3 | 半路杀出     |
|  4 | 共孙俪    |        5 | NULL | NULL         |
+----+-----------+----------+------+--------------+
右外连接: outer 可以省略不写,多个右表的数据
select * from hero right outer join gongfu on hero.kongfuid=gongfu.id;
select * from hero right join gongfu on hero.kongfuid=gongfu.id;
+------+-----------+----------+----+--------------+
| id   | name      | kongfuid | id | kongfu       |
+------+-----------+----------+----+--------------+
|    1 | 妲己      |        2 |  2 | 推心置腹     |
|    2 | 李白      |        1 |  1 | 吟诗作对     |
|    3 | 程咬金    |        3 |  3 | 半路杀出     |
| NULL | NULL      |     NULL |  4 | 沉默是金     |
+------+-----------+----------+----+--------------+

注意:cross join  使用的时候就不能再加left或者right 还有outer这些关键字了
select * from hero cross join gongfu on hero.kongfuid=gongfu.id;
+----+-----------+----------+----+--------------+
| id | name      | kongfuid | id | kongfu       |
+----+-----------+----------+----+--------------+
|  2 | 李白      |        1 |  1 | 吟诗作对     |
|  1 | 妲己      |        2 |  2 | 推心置腹     |
|  3 | 程咬金    |        3 |  3 | 半路杀出     |
+----+-----------+----------+----+--------------+

# 自连接: 一种特殊的连接,连接需要对左表和右表分别起别名<左表和右表是同一个表>
注意:必须起别名,as可以省略.
1.>汇总的数据来自一张表的时候.

步骤:
1.>areas.sql文件拷贝到linux桌面
2.>进入桌面:cd ~/Desktop
3.>登录mysql
4.>选择数据库 use py_test
5.>创建表
create table areas(
aid int primary key,
atitle varchar(20),
pid int
);
6.>在 mysql命令终端下面执行 source F:/areas.sql 这样就把数据导入到库中了.

形式: select * from 表 as 别名1 join 表 as 别名2 on 别名1.字段= 别名2.字段;
查询笛卡尔积的记录数量:
select count(*) from areas pro join areas city;
# 查询深圳市下属所有区
select *  from areas pro join areas city on city.pid = pro.aid where pro.atitle='深圳市';
+--------+-----------+--------+--------+-----------+--------+
| aid    | atitle    | pid    | aid    | atitle    | pid    |
+--------+-----------+--------+--------+-----------+--------+
| 440300 | 深圳市    | 440000 | 440303 | 罗湖区    | 440300 |
| 440300 | 深圳市    | 440000 | 440304 | 福田区    | 440300 |
| 440300 | 深圳市    | 440000 | 440305 | 南山区    | 440300 |
| 440300 | 深圳市    | 440000 | 440306 | 宝安区    | 440300 |
| 440300 | 深圳市    | 440000 | 440307 | 龙岗区    | 440300 |
| 440300 | 深圳市    | 440000 | 440308 | 盐田区    | 440300 |
+--------+-----------+--------+--------+-----------+--------+


子查询:select的嵌套

select 里面嵌入另外一个select查询

分类:
标量子查询:子查询的结果是一个数据<一行或一列>  返回的查询结果是一个数,一个值
行子查询:返回的结果是一行
列子查询:返回的结果是一列

表子查询:返回的结果是一个表

标量子查询:最高身高的姓名
select name from students where height = (select max(height) from students);
+-----------+
| name      |
+-----------+
| 彭于晏    |
+-----------+
高于平均身高的.  也是一个标量子查询
mysql> select name from students where height >= (select avg(height) from students);
+-----------+
| name      |
+-----------+
| 小明      |
| 小月月    |
| 彭于晏    |
| 刘德华    |
| 程坤      |
| 静香      |
| 周杰      |
+-----------+

行子查询:返回的结果是一行. 求身高最高并且年龄最大的.  注意:这里拿元组类型来接收(height,age)=(185.00,59)
select * from students where (height,age) =  (select max(height),max(age) from students);
+----+-----------+------+--------+--------+--------+-----------+
| id | name      | age  | height | gender | cls_id | is_delete |
+----+-----------+------+--------+--------+--------+-----------+
|  4 | 刘德华    |   59 | 185.00 | 男     |      2 |          |
+----+-----------+------+--------+--------+--------+-----------+

列子查询:返回的结果是一列  找出已经开班班级的所有学生信息
select id from classes---> 返回的结果是一列


select * from students where cls_id in (select id from classes);
+----+-----------+------+--------+--------+--------+-----------+
| id | name      | age  | height | gender | cls_id | is_delete |
+----+-----------+------+--------+--------+--------+-----------+
|  1 | 小明      |   18 | 180.00 | 女     |      1 |           |
|  2 | 小月月    |   18 | 180.00 | 女     |      2 |          |
|  3 | 彭于晏    |   29 | 185.00 | 男     |      1 |           |
|  4 | 刘德华    |   59 | 185.00 | 男     |      2 |          |
|  5 | 黄蓉      |   38 | 160.00 | 女     |      1 |           |
|  6 | 凤姐      |   28 | 150.00 | 保密   |      2 |          |
|  7 | 王祖贤    |   18 | 172.00 | 女     |      1 |          |
|  8 | 周杰伦    |   36 |   NULL | 男     |      1 |           |
|  9 | 程坤      |   27 | 181.00 | 男     |      2 |           |
| 10 | 刘亦菲    |   25 | 166.00 | 女     |      2 |           |
+----+-----------+------+--------+--------+--------+-----------+


总结:等下回去看
关键字顺序:
 select * from 表名 
 [join 表名] 
 [on 连接条件] 
 [where 条件判断] 
 [group by 字段名] [asc|desc],...字段名 [asc|desc]...
 [having 条件判断]
 [order by 字段名 ][asc|desc] 
 [limit 起始位置,每一页显示的数据个数]


"""
"""
SQL	语句的完整格式:

SELECT select_expr [,select_expr,...] [      
      FROM tb_name
      [JOIN 表名]
      [ON 连接条件] 
      [WHERE 条件判断]
      [GROUP BY {col_name | postion} [ASC | DESC], ...] 
      [HAVING 条件判断]
      [ORDER BY {col_name|expr|postion} [ASC | DESC], ...]
      [ LIMIT {[offset,]rowcount | row_count OFFSET offset}]
]

示例:
select price, group_concat(name) from goods group by price desc;
+-----------+---------------------------------------+
| price     | group_concat(name)                    |
+-----------+---------------------------------------+
| 28888.000 | mac pro专业级台式电脑                 |
|  9188.000 | imac me086ch/a 21.5英寸一体电脑       |
|  8499.000 | g150th 15.6英寸游戏本                 |
|  7999.000 | svp13226scb 触控超极本                |
|  6999.000 | hmz-t3w 头戴显示设备                  |
|  6888.000 | x3250 m4机架式服务器                  |
|  5388.000 | poweredge ii服务器                    |
|  4999.000 | y400n 14.0英寸笔记本电脑              |
|  4880.000 | x240 超极本                           |
|  4299.000 | u330p 13.3英寸超极本                  |
|  4288.000 | z220sff f4f06pa工作站                 |
|  3699.000 | at7-7414lp 台式电脑 linux ）          |
|  3499.000 | ideacentre c340 20英寸一体电脑        |
|  3399.000 | r510vc 15.6英寸笔记本                 |
|  3388.000 | ipad air 9.7英寸平板电脑              |
|  2899.000 | vostro 3800-r1206 台式电脑            |
|  2799.000 | x550cc 15.6英寸笔记本                 |
|  2788.000 | ipad mini 配备 retina 显示屏          |
|  1998.000 | ipad mini 7.9英寸平板电脑             |
|    99.000 | 商务双肩背包,商务双肩背包             |
+-----------+---------------------------------------+

PS:注意:mysql中没有top关键字命令,top是oracle的. 类似top的功能是limit命令
示例:取出倒数10个:
select * from 表名 order by 字段名 desc limit 10;
"""
# -----------------------navicat 常用快捷键----------------------------->
"""
Navicat常用快捷键

1，Ctrl+q就会弹出一个sql输入窗口 
2，Ctrl+r就执行sql了 
3，按F6会弹出一个命令窗口 ----> 这样就是类似在mysql的shell界面下进行操作了.
4，Ctrl+/ 注释 
5，Ctrl +Shift+/ 解除注释 
6，Ctrl+R 运行选中的SQL语句 
7，Ctrl+Shift+R 只运行选中的sql语句 
8，Ctrl+L 删除选中行内容 
9，Ctrl+D 表的数据显示显示页面切换到表的结构设计页面，但是在查询页面写sql时是复制当前行并粘贴到下一行 
10，Ctrl+N 打开一个新的查询窗口 
11，Ctrl+W 关闭当前查询窗口 
12，鼠标三击选择当前行

"""