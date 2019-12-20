"""
数据库:数据的集合. 特点: 高效的管理数据   数据库本身就是一种文件.
特点:
1.>持久化存储
2.>读写速度极高
3.>保证数据的有效性  防止数据错误<类型 约束>
4.>对程序支持性非常好,容易扩展  mysql
"""

"""
数据库客户端-->数据库服务器-->数据库文件文件

数据库文件才是存储数据的,接受服务器取数据的请求

客户端 接收用户的请求

服务器:接收客户端请求,从数据库文件中读取数据 .提供数据服务

DBMS:
SQL: 就是一坨字符串,一种语法

关系型数据库:RDBMS 通用语法是SQL

数据库面试时最基础的,必须会手写

关系模型:借助集合代数等数学概念. 本质上使用一张二维表来表示关系<和excel一样>





oracle:银行,电信等项目  收费按cpu核心数计算  能够接收的客户端数量来收费

ms sql server:微软

sqlite: 轻量级

mysql:web时代使用最广泛  提供社区版/收费版本

横行竖列:

数据行:记录
数据列:字段
数据表:整个表
表结合表:数据库

DB2:IBM的原创
DQL:查询,select
DML:操作,增加,修改,delete删除
对于WEB程序员而言:crud:增删改查
注意:不区分大小写  关键字是大写 只是为了区分的更清楚,给人看而已

"""
# --------------------------------安装启动------------------------------->
"""
安装:
服务器:
sudo apt-get install mysql-server
客户端:
sudo apt-get install mysql-client
判断服务是否启动:<最常用的>
ps aux | grep mysql   --->mysqld的服务
或者:
sudo service mysql status    查看状态  <最常用>
sudo service mysql restart   重启
sudo service mysql stop      停止
sudo service mysql start     启动

日志:程序的日志

启动navicat,cd 切换到在Desktop,继续cd 进入 navicat的目录
输入./start_navicat命令启动navicat即可.

"""
# ----------------------------------数据类型----------------------------------------------------------------------->
"""
数据类型和约束:
数据类型:对数据的要求,影响着数据中存储的数据所占的类型约束,空间大小
约束:数据类型之外添加额外的要求

原则:够用就行,尽量省空间
int:4个字节bytes
bit<只能存一个0或者1,就是一个最小的存储空间>:表示true或者false的状态,真假,是否,存储互斥关系
unsigned: 非负数
1bytes=8bit
decimal:小数,decimal(5,2),表示共存5位数,小数占2位,都是最多
varchar:不定长 用多少给多少,但是不能超过最长的限制 varchar(3):表示最长是3个字节
char:定长 char(32) 32个字节长度的char  张三 <6个字节>  造成空间的浪费 一般比较少用,用于手机号/身份证号等固定长度的
图片/音频/视频/等,数据库存储对应的路径
text字符串存储大文本,超过4000的时候推荐使用,比如技术博客
date/time/datetime
枚举(enum):提前把要用的都列出来,比如性别类型 {'男','女','中性',未知}
有符号:有-号,可以表示负数
无符号:0和整数

smallint:表示port端口数  0-65535 的范围,刚刚好可以表示

text:0-65535 
timestamp:时间戳  unix时间 从1970年开始计算 

选择数据类型的要求:合适的,空间最小的.

"""
# ----------------------------------数据类型的约束-------------------------------------------------------------------------->
"""
约束:保证数据的完整性.必须要填的,可以不填的这种
主键:primary key 唯一的标识  主键约束  都要有主键,mysql的 要求
作用:唯一标识一行记录.一般都是id 自增的整数
非空:not null 此字段不允许为空值
唯一 unique:此字段值不允许重复 身份证号是unique的约束
默认 default:某一个字段不填的时候,设计者自己会给这个字段填一个默认值
如果用户没有填,使用默认值,如果填了,就使用用户填的.
外键 foreign key: 一个表中存了另外一个表的id
A表中的A字段使用了B表中的B字段.外键约束的含义是A字段的值必须在B字段出现过.
A字段的值必须是B字段中的子集<不能试B字段中没有的>

"""
"""
操作:
创建数据库
创建表结构<没有表数据>  字段名 类型 约束
操作表数据

"""
# ----------------------------------------------------登录/退出 数据库操作---------------------------------------------------->
"""
登录:linux里面的
mysql -uroot -p 密码  或者  mysql -u root -p 密码   有没有空格都行,mysql会自己解析出来.
mysql -uroot -p 在后面输入密码不会显示

退出:这些操作是在mysql的shell界面进行操作
exit
quit
Ctrl+d  ---> 快捷键 
"""
# ---------------------------------------------------数据库操作指令/创建,使用,查看------------------------------------------------>
"""
数据库操作:

1.>展示所有的数据库:show databases; 记得加s,加;分号

2.>切换指定数据库:use + 数据库名字;

3.>查看当前正在使用的数据库:select database(); 注意:这个是单数,database没有s

ps: 输入指令不完全的时候继续往下输就行,系统会自己填.

4.create database 数据库名字 charset=utf8; 千万不能在utf8中间写-,不可以是utf-8这种格式.

如果不设置 charset,默认是另外一种格式 latin1 拉丁字符集<英文,德文,法文>,不能存储汉字类型的字符,比如日文,韩文等等.

5.>展示创建数据库的SQL过程:show create database 数据库名字;

6.>展示当前数据库中的所有表:show tables;

7.>查看表结构:desc + 表名字; desc是描述describe的意思.

8.>创建表结构的语法:
create table 表名字(字段 类型 [约束],...);  []里面的表示可选,意思就是可要可不要,看需求

示例:
create table studenst(
    -> id int unsigned primary key auto_increment,  -->自增就保证了id 唯一unique的约束了,也保证了not null的约束了.
    -> name varchar(32) not null,
    -> age tinyint unsigned default 0  ---> 最后一个字段不要加,号
    -> );  ----> 记得加;号结束
    
注意:创建表之后表中是没有数据的.

9.>修改表结构:
	1.alter table 表名 add 字段名<就是列名> 类型 约束;-->增加一个字段
		比如: alter table student add birthday datetime not null;添加一个字段birthday,类型datetime约束是not null.
	2.alter table 表名 change 原字段名 新字段名 类型 约束;-->修改字段名称 类型 或者约束
		alter table student change birthday birth date;
	3.alter table 表名 modify 字段名 新类型 新约束;-->只修改<字段名称不修改> 类型 或者约束
		alter table student modify birth date not null;
	4.alter table 表名 drop 字段名;-->删除字段
		alter table student drop birth;
		
ps:将原来的 '列名' 叫法 ---> 记得转换为叫 字段名.这些都是为了以后工作沟通方便<mysql里面列称之为字段,行称之为记录>.

10.>展示创建数据表的SQL过程:
	show create table students;
	
11.>删除表:
	drop table students;
	
"""
# ---------------------------------------------------操作表数据:增删改查------------------------------------------------------------>
"""操作表数据:

增删改查:
					标识数据的字段顺序  加s的可以插入多行数据
1.>增加:<插入>

insert into 表名(字段名1,字段名2...) values/value (1,28,'Jerry'),(),(),()...

insert into 表名(id,age,name) values/value (1,28,'Jerry'),(),(),()...
	
如果 values()里面的数据顺序和字段顺序一致,可以不写字段顺序

eg:insert into student(id,age,name) values (1,28,'Tom');
	insert into student values (1,28,'Tom');
	
如果希望使用字段的默认值,使用null 或者 0<主键还可以使用自动增长> :

insert into student(id,age,name) values (0,28,'Tom'); 
insert into student(age,name) values (28,'Tom'); 

ps:<id最常用,可以直接写0,默认是自增或者延续之前的字段规律>

2.>查询:

select * from 表名字;  * 代表所有字段

查询指定字段:
select 字段1,字段2 from 表名字;

3.>更新:

update 表名字 set 字段名1=新值1,字段名2=新值2 where 条件;

如果不写where 条件 这部分,默认是把所有行记录进行修改.那将是什么样的后果???,以后千万不要这么操作

 update studenst set name='胡锦涛' where id=3;
 update studenst set name='李斌',age=25 where id=2;
 
 注意:一定要加where 条件部分.

4.>删除:

delete from 表名 where 条件;  --->物理删除

drop table 表  ------> 表名,表结构等等全部删除

where 是用于 挑选满足条件的 记录 (元组)

不加条件就是全部.
这种删除数据是很难恢复的  --->物理删除

逻辑删除 --> 标记:在显示的时候带有标记的不显示

本质上是更新操作.

先要添加一个标记is_delete表示是否被删除:alter table studenst add is_delete bit default 0;

工作中也是建议使用逻辑删除.反正删除这种操作时非常谨慎的东西,千万不要冲动.

注意:如果设置了default 就不再需要设置not null 约束了.因为默认值存在,就不会有空值了.
"""
